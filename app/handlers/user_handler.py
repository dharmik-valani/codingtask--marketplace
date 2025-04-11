from flask import request, jsonify, current_app
from app.services.user_service import UserService
from app.utils.jwt_utils import generate_jwt_token

def register_user_handler(user_service: UserService):

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or len(username) < 3:
        return jsonify({'error': 'Invalid username'}), 400

    if not email or '@' not in email:
        return jsonify({'error': 'Invalid email'}), 400

    if not password or len(password) < 6:
        return jsonify({'error': 'Password too short'}), 400

    try:
        user = user_service.register_user(username, email, password)
        return jsonify({"message": "User registered successfully", "user": {
            "id": user.id,
            "email": user.email,
        } }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def login_user_handler(user_service: UserService):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    try:
        user = user_service.login_user(username, password)

        token = generate_jwt_token({'username': user.username})

        return jsonify({
            "message": "Login successful",
            "token": token
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
