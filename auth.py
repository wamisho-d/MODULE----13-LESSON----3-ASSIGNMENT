# Task 3: Authentication Logic: Create the auth.py file for managing authentication.

from flask import Blueprint, request, jsonify
from models import User, db
from utils.util import encode_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        token = encode_token(user.id)
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
