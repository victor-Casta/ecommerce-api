from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Lista de categorías
categories = [
    {
        "id": 1,
        "name": "Shirts",
        "products": ["T-Shirt", "Polo Shirt", "Button-Up Shirt", "Hawaiian Shirt", "Shirt Black"],
    },
    {
        "id": 2,
        "name": "Pants",
        "products": ["Jeans", "Chinos", "Cargo Pants", "Shorts"],
    },
    {"id": 3, "name": "Outerwear", "products": ["Jacket", "Coat"]},
]

# Lista de productos
# Lista de productos con descripciones añadidas
products = [
    {
        "id": 1,
        "name": "T-Shirt",
        "category": "Shirts",
        "subCategory": ["menswear"],
        "price": 19.99,
        "pricePerUnit": 19.99,
        "image": "https://contents.mediadecathlon.com/p2436315/e957bd6a23553ffabaef22fd550e99c3/p2436315.jpg",
        "description": "A classic and comfortable T-Shirt made from 100% cotton. Perfect for everyday wear.",
    },
    {
        "id": 2,
        "name": "Polo Shirt",
        "category": "Shirts",
        "subCategory": ["menswear"],
        "price": 24.99,
        "pricePerUnit": 24.99,
        "image": "https://marcopolo.dam.aboutyou.cloud/images/images/b8a7a715945def86723768adfeaff077.jpg",
        "description": "A versatile Polo Shirt, great for casual and semi-formal occasions. Made with breathable fabric.",
    },
    {
        "id": 3,
        "name": "Button-Up Shirt",
        "category": "Shirts",
        "subCategory": ["menswear"],
        "price": 29.99,
        "pricePerUnit": 29.99,
        "image": "https://www.gluestore.com.au/cdn/shop/products/IMG_7970_8fb3bae7-e6fa-4dc6-b4a4-d52969080c5c_1600x.jpg",
        "description": "A stylish Button-Up Shirt suitable for both formal and casual settings. Crafted from premium material.",
    },
    {
        "id": 4,
        "name": "Hawaiian Shirt",
        "category": "Shirts",
        "subCategory": ["menswear", "sale"],
        "price": 34.99,
        "pricePerUnit": 34.99,
        "image": "https://images.lee.com/is/image/Lee/112350382-HERO?$KDP-XLARGE$",
        "description": "A vibrant Hawaiian Shirt perfect for vacations or casual summer outings. Made with soft, lightweight fabric.",
    },
    {
        "id": 5,
        "name": "Jeans",
        "category": "Pants",
        "subCategory": ["menswear"],
        "price": 39.99,
        "pricePerUnit": 39.99,
        "image": "https://i.pinimg.com/736x/8e/8d/19/8e8d19acba343386d4cc1f917bf80995.jpg",
        "description": "Durable and stylish Jeans that provide comfort and style for any casual look. Available in multiple shades.",
    },
    {
        "id": 6,
        "name": "Chinos",
        "category": "Pants",
        "subCategory": ["menswear", "sale"],
        "price": 34.99,
        "pricePerUnit": 34.99,
        "image": "https://www.creaturesofhabit.in/cdn/shop/files/Graphite_S_20155743_1.jpg",
        "description": "Comfortable and versatile Chinos, ideal for both work and casual occasions. Made with high-quality fabric.",
    },
    {
        "id": 7,
        "name": "Cargo Pants",
        "category": "Pants",
        "subCategory": ["menswear"],
        "price": 44.99,
        "pricePerUnit": 44.99,
        "image": "https://i8.amplience.net/i/jpl/jd_703958_a",
        "description": "Stylish Cargo Pants with multiple pockets for practicality. Great for outdoor activities and casual wear.",
    },
    {
        "id": 8,
        "name": "Shorts",
        "category": "Pants",
        "subCategory": ["womenswear"],
        "price": 29.99,
        "pricePerUnit": 29.99,
        "image": "https://cdn.baguer.co/uploads/2023/09/short-para-mujer-tipo-bermuda-con-proceso-claro-unser-azul-828756AZ.jpg_eYmBrZJQLzeOZPZtD0OaepMRVYBnwaiuvxpcvGX6MSkrTeK6Wz.jpg",
        "description": "Comfortable Shorts, perfect for warm weather. Made with lightweight fabric to ensure cool comfort.",
    },
    {
        "id": 9,
        "name": "Coat",
        "category": "Outerwear",
        "subCategory": ["menswear", "sale"],
        "price": 99.99,
        "pricePerUnit": 99.99,
        "image": "https://strellson.com/medias/sys_master/images/images/hea/h5c/9884572975134/9884572975134.jpg",
        "description": "A premium winter Coat that offers warmth and style. Crafted from durable materials for harsh weather.",
    },
    {
        "id": 10,
        "name": "Jacket",
        "category": "Outerwear",
        "subCategory": ["menswear"],
        "price": 79.99,
        "pricePerUnit": 79.99,
        "image": "https://media.boohoo.com/i/boohoo/bmm57373_black_xl/male-black-lightweight-bomber-jacket-in-black/?w=900&qlt=default&fmt.jp2.qlt=70&fmt=auto&sm=fit",
        "description": "A trendy lightweight Jacket that is perfect for layering. Ideal for cool evenings and casual outings.",
    },
        {
        "id": 11,
        "name": "Shirt Black",
        "category": "Shirts",
        "subCategory": ["womenswear"],
        "price": 29.99,
        "pricePerUnit": 29.99,
        "image": "https://www.albaray.co.uk/cdn/shop/files/5056487359679_1.jpg?v=1706622967&width=1000",
        "description": "Experience ultimate comfort in our best-selling T shirt featuring drop shoulders and roll back cuffs.",
    },
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
