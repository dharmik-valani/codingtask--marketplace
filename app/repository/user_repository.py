from app.models.user import User

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_user_by_username(self, username):
        query = f"SELECT username, email, password_hash FROM users WHERE username = '{username}'"
        result = self.db_session.execute(query).fetchone()
        if result:
            return User(result['username'], result['email'], result['password'])
        return None

    def create_user(self, user):
        self.db_session.execute(
            "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)",
            {"username": user.username, "email": user.email, "password": user.password}
        )
        self.db_session.commit()
