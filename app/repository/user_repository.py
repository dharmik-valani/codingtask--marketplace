from app.models.user import User
from sqlalchemy import text

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_user_by_username(self, username):
        return self.db_session.query(User).filter_by(username=username).first()

    def create_user(self, user):
        self.db_session.add(user)
        self.db_session.commit()

