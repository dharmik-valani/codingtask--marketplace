from flask import request, jsonify
from app.services.user_service import UserService

def register_user_handler(user_service: UserService):
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400

    if 'username' not in data or len(data['username']) < 3:
        return jsonify({'error': 'Invalid username'}), 400

    if 'email' not in data or '@' not in data['email']:
        return jsonify({'error': 'Invalid email'}), 400

    if 'password' not in data or len(data['password']) < 6:
        return jsonify({'error': 'Password too short'}), 400
    
    try:
        user_service.register_user(data['username'], data['email'], data['password'])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify({"message": "User registered successfully"}), 201

def login_user_handler(user_service: UserService):
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    try:
        user = user_service.login_user(data['username'], data['password'])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify({"message": "Login successful", "username": user.username}), 200
