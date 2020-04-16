from models import User
from quart import Blueprint, request, jsonify
from quart.helpers import make_response
from db import Session

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
async def register():
    # get the post data
    post_data = await request.get_json()
    # check if user already exists
    user = Session.query(User).filter_by(email=post_data.get('email')).first()
    if not user:
        user = User(
            email=post_data.get('email'),
            password=post_data.get('password')
        )
        # insert the user
        Session.add(user)
        Session.commit()

        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        responseObject = {
            'status': 'success',
            'message': 'Successfully registered.',
            'auth_token': auth_token.decode()
        }
        return await make_response(jsonify(responseObject)), 201
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return await make_response(jsonify(responseObject)), 202

@auth_blueprint.route('/login', methods=['POST'])
async def login():
    post_data = await request.get_json()
    email= post_data.get('email')
    password= post_data.get('password')
    # fetch the user data
    try:
        user = Session.query(User).filter_by(email=email).first()
        hash_password = User.hash_password(password)
        if hash_password == user.password:
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
                return await make_response(jsonify(responseObject)), 200
        return await make_response('Authentication Error'), 403
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return await make_response(jsonify(responseObject)), 500