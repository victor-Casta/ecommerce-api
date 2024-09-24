from flask import Flask, jsonify, request
app =  Flask(__name__)

@app.route('/')
def hello():
  return 'Hello, World!'

@app.route('/products/<product_id>')
def get_products(product_id):
  products = [
    {'id': product_id, 'name': 'Product 1', 'price': 19.99},
  ]
  query = request.args.get('query')
  if query:
    products.append(query)
  return jsonify(products), 200

if __name__ == '__main__':
  app.run(debug=True)