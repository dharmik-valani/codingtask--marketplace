from main import app, db
from app.handlers.user_handler import register_user_handler, login_user_handler
from app.handlers.product_handler import add_product_handler, list_products_handler
from app.repository.user_repository import UserRepository
from app.repository.product_repository import ProductRepository
from app.services.user_service import UserService
from app.services.product_service import ProductService

db_session = db.session

# Repositories and services setup
user_repository = UserRepository(db_session)
product_repository = ProductRepository(db_session)
user_service = UserService(user_repository)
product_service = ProductService(product_repository)

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    return register_user_handler(user_service)

@app.route('/login', methods=['POST'])
def login_user():
    return login_user_handler(user_service)

@app.route('/products', methods=['POST'])
def add_product():
    return add_product_handler(product_service)

@app.route('/products', methods=['GET'])
def list_products():
    return list_products_handler(product_service)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)