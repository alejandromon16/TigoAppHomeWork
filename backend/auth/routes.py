from flask import Blueprint, request, jsonify
from auth.user_store import UserStore

bp = Blueprint('auth', __name__)
user_store = UserStore()

@bp.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']
    display_name = request.json['display_name']
    if user_store.register_user(email, password, display_name):
        auth_token = 'generate your auth token here'
        return jsonify({'auth_token': auth_token}), 201
    else:
        return jsonify({'message': 'Email already exists'}), 400

@bp.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    display_name = user_store.authenticate_user(email, password)
    if display_name is None:
        return jsonify({'message': 'Invalid credentials or user already logged in'}), 401
    auth_token = 'generate your auth token here'
    return jsonify({'auth_token': auth_token}), 200

@bp.route('/logout', methods=['POST'])
def logout():
    email = request.json['email']
    if user_store.logout_user(email):
        return jsonify({'message': 'User logged out'}), 200
    else:
        return jsonify({'message': 'User not logged in'}), 400
