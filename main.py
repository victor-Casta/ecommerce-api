from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Lista de categorías
categories = [
  {
    'id': 1,
    'name': 'Shirts',
    'products': ['T-Shirt']
  },
  {
    'id': 2,
    'name': 'Pants',
    'products': ['Pants']
  },
  {
    'id': 3,
    'name': 'Outerwear',
    'products': ['Jacket']
  }
]

# Lista de productos
products = [
    {
      'id': 1,
      'name': 'T-Shirt',
      'category': 'Shirts',
      'price': 19.99,
      'image': 'https://images.pexels.com/photos/428340/pexels-photo-428340.jpeg'
    },
    {
      'id': 2,
      'name': 'Jeans',
      'category': 'Pants',
      'price': 39.99,
      'image': 'https://images.pexels.com/photos/2897521/pexels-photo-2897521.jpeg'
    },
    {
      'id': 3,
      'name': 'Jacket',
      'category': 'Outerwear',
      'price': 59.99,
      'image': 'https://images.pexels.com/photos/28561358/pexels-photo-28561358.jpeg'
    }
]

# Ruta para obtener todas las categorías
@app.route('/categories', methods=['GET'])
def get_all_categories():
    return jsonify(categories), 200

# Ruta para obtener todos los productos
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(products), 200

# Ruta para obtener una categoría específica por su id
@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = next((item for item in categories if item['id'] == category_id), None)
    if category:
        return jsonify(category), 200
    else:
        return jsonify({'error': 'Category not found'}), 404

# Ruta para obtener un producto específico por su id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
