import re
from flask_restful import Resource, reqparse, inputs
from models import UserModel, RevokedTokenModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from PDF_Creator import *
from config import ALEXA_SECRET_KEY
from config import VALID_JOINTS

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', help = 'Email is required', required = True)
login_parser.add_argument('password', help = 'Password is required', required = True)

alexa_heatmap_parser = reqparse.RequestParser()
alexa_heatmap_parser.add_argument('location', help = 'Location is required', required = True)
alexa_heatmap_parser.add_argument('email', help = 'Email is required', required = True)
alexa_heatmap_parser.add_argument('password', help = 'Password is required', required = True)

user_heatmap_parser = reqparse.RequestParser()
user_heatmap_parser.add_argument('location', help = 'Location is required', required = True)

user_medication_parser = reqparse.RequestParser()
user_medication_parser.add_argument('medication', help = 'Medication is required', required = True)

registration_parser = reqparse.RequestParser()
registration_parser.add_argument('email', help = 'Email is required', required = True)
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
            return {'message': 'User {} already exists'.format(data['email'])}, 400
        
        new_user = UserModel(
            email = data['email'],
            password = UserModel.generate_hash(data['password']),
            first_name = data['first_name'],
            last_name = data['last_name'],
            phone = data['phone'],
            gender = data['gender'],
            dob = data['dob'],
            dod = data['dod'],
            medications = [],
            heatmap = []
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
        except Exception as e:
            print(e)
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
            #return {"pdf":export("{} {}".format(data.first_name, data.last_name), [])}
            return {"pdf":export()}
        return {'message': 'could not find your data'}, 404

class Heatmap(Resource):
    # this put is from alexa
    def put(self):
        data = alexa_heatmap_parser.parse_args()
        user = UserModel.find_by_email(data['email'])
        if not user:
            return {'message': 'User {} not found'.format(data['email'])}, 404
        if data['password'] != ALEXA_SECRET_KEY:
            return {'message': 'password invalid'}, 400
        if data['location'] not in VALID_JOINTS:
            print("invalid location: " + data['location'])
            # return {'message': 'location invalid'}, 400
        user.heatmap.append(data['location'])
        user.save_to_db()
        return {'message': 'added to heatmap'}
    # this post is from a user
    @jwt_required
    def post(self):
        user = UserModel.find_by_email(get_jwt_identity())
        if not user:
            return {'message': 'User not found'}, 404
        data = user_heatmap_parser.parse_args()
        print("location: " + data['location'])
        user.heatmap.append(data['location'])
        user.save_to_db()
        return {'message': 'added to heatmap'}

class Medications(Resource):
    @jwt_required
    def put(self):
        user = UserModel.find_by_email(get_jwt_identity())
        if not user:
            return {'message': 'User not found'}, 404
        data = user_medication_parser.parse_args()
        print("medication: " + data['medication'])
        user.medications.append(data['medication'])
        user.save_to_db()
        return {'message': 'added to medications'}
