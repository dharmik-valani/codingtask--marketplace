from main import db
from sqlalchemy.orm import declarative_base

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    seller_id = db.Column(db.Integer, nullable=False)

    def __init__(self, title, description, price, seller_id):
        self.title = title
        self.description = description
        self.price = price
        self.seller_id = seller_id
