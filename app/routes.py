from flask import Blueprint, current_app, request, jsonify
from app.extensions import db
from app.models import User
from app.utils import hash_password, check_password, generate_jwt
import jwt

bp = Blueprint('auth', __name__)

@bp.route('/')
def index():
    return 'Auth System is running!'

@bp.route('/profile', methods=['GET'])
def profile():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({'message': 'Missing authorization header'}), 401

    try:
        token = auth_header.split(" ")[1]  # "Bearer <token>"
        decoded = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded['user_id']

        # Optionally, fetch user from database
        from app.models import User
        user = User.query.get(user_id)

        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return jsonify({'message': 'Invalid or expired token'}), 401

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'message': 'Username or email already exists'}), 400

    new_user = User(username=username, email=email, password_hash=hash_password(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password(password, user.password_hash):
        return jsonify({'message': 'Invalid username or password'}), 401

    token = generate_jwt({'user_id': user.id}, expires_in=3600)
    return jsonify({'access_token': token}), 200
