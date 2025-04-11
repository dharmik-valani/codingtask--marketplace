from app.models.product import Product
from app.repository.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def add_product(self, title, description, price, seller_id):
        product = Product(title, description, price, seller_id)

        if title is None or title.strip() == "":
            raise ValueError("Product title cannot be empty.")
        
        blacklist = ["banned", "illegal", "restricted"]
        if any(banned_word in title.lower() for banned_word in blacklist):
            raise ValueError("Product title contains restricted words.")

        if price is None or price < 0:
            raise ValueError("Product price must be a positive value.")

        if description and len(description) > 255:
            raise ValueError("Product description cannot exceed 255 characters.")

        self.product_repository.add_product(product)

    def list_products(self):
        # return self.product_repository.get_all_products(limit=20)
        return self.product_repository.get_all_products()

    def delete_product(self, product_id):
        if product_id is None:
            raise ValueError("Invalid product ID")
        self.product_repository.delete_product_by_id(product_id)
