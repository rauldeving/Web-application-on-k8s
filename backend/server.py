from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert_form')
def insert_data():
    return render_template('insert_form.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        product_name = request.form['product_name']
        price = request.form['price']
        quantity = request.form['quantity']

        print(f"Received product: {product_name}, {price}, {quantity}")
        return render_template('insert_form.html', message="Data inserted successfully!")


@app.route('/show_data')
def show_data():
    data = [
        {'id': 1, 'product_name': 'Product 1', 'price': 100, 'quantity': 10},
        {'id': 2, 'product_name': 'Product 2', 'price': 150, 'quantity': 20},
    ]
    return render_template('show_data.html', data=data)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
