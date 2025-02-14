from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)


products = []

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
        

        product = {
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }
        products.append(product)
        return render_template('insert_form.html', message="Product added successfully!")

@app.route('/show_data')
def show_data():
    
    return render_template('show_data.html', data=products)

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
  
