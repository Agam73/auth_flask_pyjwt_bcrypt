import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import current_app

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def generate_jwt(payload, expires_in=3600):
    payload['exp'] = datetime.utcnow() + timedelta(seconds=expires_in)
    return jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
