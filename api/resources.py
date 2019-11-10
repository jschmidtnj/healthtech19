import re
from flask_restful import Resource, reqparse, inputs
from models import UserModel, RevokedTokenModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from PDF_Creator import *

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', help = 'Email is required', required = True)
login_parser.add_argument('password', help = 'Password is required', required = True)

registration_parser = reqparse.RequestParser()
registration_parser.add_argument('email', help = 'Email is required', required = True, type=inputs.regex("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"))
registration_parser.add_argument('password', help = 'Password is required', required = True)
registration_parser.add_argument('first_name', help = 'First name is required', required = True)
registration_parser.add_argument('last_name', help = 'Last name is required', required = True)
registration_parser.add_argument('phone', help = 'Phone is required', required = True)
registration_parser.add_argument('dob', help = 'Date of birth is required', required = True)
registration_parser.add_argument('dod', help = 'Date of diagnosis is required', required = True)
registration_parser.add_argument('gender', help = 'Gender is required', required = True)

class UserRegistration(Resource):
    def post(self):
        data = registration_parser.parse_args()
        
        if UserModel.find_by_email(data['email']):
            return {'message': 'User {} already exists'.format(data['email'])}
        
        new_user = UserModel(
            email = data['email'],
            password = UserModel.generate_hash(data['password']),
            first_name = data['first_name'],
            last_name = data['last_name'],
            phone = data['phone'],
            gender = data['gender'],
            dob = data['dob'],
            dod = data['dod']
        )
        
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'User {} was created'.format(data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def put(self):
        data = login_parser.parse_args()
        current_user = UserModel.find_by_email(data['email'])

        if not current_user:
            return {'message': 'invalid email or password'}, 400
        
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'Logged in as {}'.format(current_user.email),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'invalid email or password'}, 400


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

class GetUser(Resource):
    @jwt_required
    def get(self):
        data = UserModel.find_by_email(get_jwt_identity())
        if data:
            return UserModel.to_json(data)
        return {'message': 'could not find your data'}, 404


class AllUsers(Resource):
    @jwt_required
    def get(self):
        return UserModel.return_all()

    @jwt_required
    def delete(self):
        return UserModel.delete_all()

class GeneratePDF(Resource):
    @jwt_required
    def get(self):
        data = UserModel.find_by_email(get_jwt_identity())
        if data:
            return {"pdf":pc.extract("{} {}".format(data.first_name, data.last_name), [])}
        return {'message': 'could not find your data'}, 404
