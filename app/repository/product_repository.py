from app.models.product import Product

class ProductRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_product(self, product):
        self.db_session.add(product)
        self.db_session.commit()

    def get_all_products(self):
        return self.db_session.query(Product).all()

    def delete_product_by_id(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if product:
            self.db_session.delete(product)
            self.db_session.commit()
            
    def get_products_by_seller(self, seller_id):
        return self.db_session.query(Product).filter_by(seller_id=seller_id).all()
