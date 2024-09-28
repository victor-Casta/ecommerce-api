from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Lista de categorías
categories = [
    {"id": 1, "name": "Shirts", "products": ["T-Shirt", "Polo Shirt", "Button-Up Shirt", "Hawaiian Shirt"]},
    {"id": 2, "name": "Pants", "products": ["Jeans", "Chinos", "Cargo Pants", "Shorts"]},
    {"id": 3, "name": "Outerwear", "products": ["Jacket", "Coat"]},
]

# Lista de productos
products = [
    {
        "id": 1,
        "name": "T-Shirt",
        "category": "Shirts",
        "price": 19.99,
        "image": "https://contents.mediadecathlon.com/p2436315/e957bd6a23553ffabaef22fd550e99c3/p2436315.jpg",
    },
    {
        "id": 2,
        "name": "Polo Shirt",
        "category": "Shirts",
        "price": 24.99,
        "image": "https://marcopolo.dam.aboutyou.cloud/images/images/b8a7a715945def86723768adfeaff077.jpg",
    },
    {
        "id": 3,
        "name": "Button-Up Shirt",
        "category": "Shirts",
        "price": 29.99,
        "image": "https://dstoreegypt.com/dstore-wp-contents/uploads/2024/04/710772290002-navy.jpeg",
    },
    {
        "id": 4,
        "name": "Hawaiian Shirt",
        "category": "Shirts",
        "price": 34.99,
        "image": "https://images.lee.com/is/image/Lee/112350382-HERO?$KDP-XLARGE$",
    },
    {
        "id": 5,
        "name": "Jeans",
        "category": "Pants",
        "price": 39.99,
        "image": "https://i.pinimg.com/736x/8e/8d/19/8e8d19acba343386d4cc1f917bf80995.jpg",
    },
    {
        "id": 6,
        "name": "Chinos",
        "category": "Pants",
        "price": 34.99,
        "image": "https://www.creaturesofhabit.in/cdn/shop/files/Graphite_S_20155743_1.jpg",
    },
    {
        "id": 7,
        "name": "Cargo Pants",
        "category": "Pants",
        "price": 44.99,
        "image": "https://i8.amplience.net/i/jpl/jd_703958_a",
    },
    {
        "id": 8,
        "name": "Shorts",
        "category": "Pants",
        "price": 29.99,
        "image": "https://cdn.baguer.co/uploads/2023/09/short-para-mujer-tipo-bermuda-con-proceso-claro-unser-azul-828756AZ.jpg_eYmBrZJQLzeOZPZtD0OaepMRVYBnwaiuvxpcvGX6MSkrTeK6Wz.jpg",
    },
    {
        "id": 9,
        "name": "Coat",
        "category": "Outerwear",
        "price": 99.99,
        "image": "https://strellson.com/medias/sys_master/images/images/hea/h5c/9884572975134/9884572975134.jpg",
    },
    {
        "id": 10,
        "name": "Jacket",
        "category": "Outerwear",
        "price": 79.99,
        "image": "https://media.boohoo.com/i/boohoo/bmm57373_black_xl/male-black-lightweight-bomber-jacket-in-black/?w=900&qlt=default&fmt.jp2.qlt=70&fmt=auto&sm=fit",
    }
]


# Ruta para obtener todas las categorías
@app.route("/categories", methods=["GET"])
def get_all_categories():
    return jsonify(categories), 200


# Ruta para obtener todos los productos
@app.route("/products", methods=["GET"])
def get_all_products():
    return jsonify(products), 200


# Ruta para obtener una categoría específica por su id
@app.route("/categories/<int:category_id>", methods=["GET"])
def get_category_by_id(category_id):
    category = next((item for item in categories if item["id"] == category_id), None)
    if category:
        return jsonify(category), 200
    else:
        return jsonify({"error": "Category not found"}), 404


# Ruta para obtener un producto específico por su id
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
