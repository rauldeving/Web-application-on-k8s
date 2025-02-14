from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

backend_url = os.getenv('BACKEND', 'http://localhost:5000/')

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
        
        response = requests.post(f"{backend_url}submit_form", data={'product_name': product_name, 'price': price, 'quantity': quantity})
               
        if response.status_code == 200:
            message = "Product added successfully!"
        else:
            message = "Failed to add product."

        return render_template('insert_form.html', message=message)

@app.route('/show_data')
def show_data():
    
    response = requests.get(f"{backend_url}show_data")
    
    if response.status_code == 200:
        data = response.json() 
        return render_template('show_data.html', data=data)
    else:
        return "Failed to fetch data"

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))  
    app.run(host=host, port=port)
