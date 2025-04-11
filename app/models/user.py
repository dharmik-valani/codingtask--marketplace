from main import db

class User(db.Model):  # Make sure it inherits from db.Model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Add this line if not present

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def check_password(self, password):
        return self.password == password
