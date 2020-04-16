import os
import bcrypt
import jwt
import datetime

from .base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = self.hash_password(password)

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=60),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        payload = jwt.decode(
            auth_token,
            os.environ.get('SECRET_KEY'),
            algorithm='HS256'
        )
        return payload['sub']

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(
            password.encode(),
            os.environ.get('BCRYPT_LOG_ROUNDS').encode()
        ).decode()