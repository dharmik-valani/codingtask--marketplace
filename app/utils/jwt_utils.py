import jwt
import datetime
from flask import current_app, request, jsonify
from functools import wraps

def decode_jwt_token(token):
    try:
        payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401

        token = auth_header.split(" ")[1]
        try:
            payload = decode_jwt_token(token)
            request.user = payload  # Optional: Attach user info
        except ValueError as e:
            return jsonify({"error": str(e)}), 401

        return f(*args, **kwargs)
    return decorated_function

def generate_jwt_token(payload: dict, expires_in_hours: int = 1) -> str:
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=expires_in_hours)
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    
    # If jwt.encode returns bytes (older PyJWT versions), decode it
    if isinstance(token, bytes):
        token = token.decode('utf-8')
        
    return token
