import jwt
import asyncio
from models import User
from quart import Blueprint, request, websocket
from quart.helpers import make_response
from functools import wraps
from urllib import parse
from db import Session

websockets_blueprint = Blueprint('websockets', __name__)

def auth_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        qs = websocket.query_string.decode()
        qs_dict = parse.parse_qs(qs)
        try:
            token_id = qs_dict.get('token_id')[0]
            email = qs_dict.get('email')[0]
        except:
            return await make_response('Bad Request'), 400

        try:
            user = Session.query(User).filter_by(email=email).first()
            user_id = User.decode_auth_token(token_id)
            if user_id == user.id:
                return await func(*args, **kwargs)
            else:
                return await make_response('Authentication Error'), 403
        except jwt.ExpiredSignatureError:
            return await make_response('Signature expired. Please log in again.'), 403
        except jwt.InvalidTokenError:
            return await make_response('Invalid token. Please log in again.'), 403
        except Exception as e:
            return await make_response('Unknown error'), 400

    return wrapper

@websockets_blueprint.websocket('/ws')
@auth_required
async def ws():
    while True:
        data = await websocket.receive()
        await websocket.send(f"echo {data}")