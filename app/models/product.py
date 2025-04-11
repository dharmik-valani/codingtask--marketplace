from main import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    seller_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, price, seller_id):
        self.name = name
        self.description = description
        self.price = price
        self.seller_id = seller_id
