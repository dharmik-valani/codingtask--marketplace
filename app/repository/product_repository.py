from app.models.product import Product
from sqlalchemy import text

class ProductRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_product(self, product):
        self.db_session.execute(
            "INSERT INTO products (title, description, price, seller_id) VALUES (:title, :description, :price, :seller_id)",
            {"title": product.title, "description": product.description, "price": product.price, "seller_id": product.seller_id}
        )
        self.db_session.commit()

    def get_all_products(self):
        results = self.db_session.execute(text("SELECT * FROM products")).fetchall()
        return [Product(result['title'], result['description'], result['price'], result['seller_id']) for result in results]

    def delete_product_by_id(self, product_id):
        self.db_session.execute(f"DELETE FROM products WHERE id = {product_id}")
        self.db_session.commit()