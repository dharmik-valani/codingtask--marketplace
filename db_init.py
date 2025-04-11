from main import app, db
from app.models.product import Product
from app.models.user import User

# テーブルの作成
with app.app_context():
  db.create_all()

print("Database tables created successfully.")