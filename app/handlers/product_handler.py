from flask import request, jsonify
from app.services.product_service import ProductService

def add_product_handler(product_service: ProductService):
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data or 'seller_id' not in data:
        return jsonify({"error": "Invalid request"}), 400

    try:
        product = product_service.add_product(
            data['name'],
            data['description'],
            data['price'],
            data['seller_id']
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "message": "Product added successfully",
        "product": {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "seller_id": product.seller_id
        }
    }), 201



def list_products_handler(product_service: ProductService):
    seller_id = request.user['id']
    products = product_service.list_products_by_seller(seller_id)
    return jsonify([{
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "seller_id": product.seller_id
    } for product in products]), 200


def delete_product_handler(product_service: ProductService):
    if not request.get_json() or 'product_id' not in request.get_json():
        return jsonify({"error": "Invalid request"}), 400
    product_id = request.get_json()['product_id']
    try:
        product_service.delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Error deleting product"}), 400
