from run import db
from passlib.hash import pbkdf2_sha256 as sha256


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    dob = db.Column(db.String(15), nullable=False)
    dod = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # medications = db.Column(db.Array(50), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def to_json(x):
        return {
            'email': x.email,
            'first_name': x.first_name,
            'last_name': x.last_name,
            'phone': x.phone,
            'gender': x.gender,
            'dob': x.dob,
            'dod': x.dod,
            'password': x.password
        }

    @classmethod
    def return_all(cls):
        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
