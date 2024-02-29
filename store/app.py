from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'such_a_very_secret_key_for_this_demo_project'

# Dummy user for demonstration purposes
USER_DATA = {
    "username": "testuser",
    "password": "password123"
}

# Dummy product data
PRODUCTS = [
    {"id": 1, "name": "Product 1", "description": "This is product 1."},
    {"id": 2, "name": "Product 2", "description": "This is product 2."}
]

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('product_listing'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_DATA['username'] and password == USER_DATA['password']:
            session['logged_in'] = True
            return redirect(url_for('product_listing'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/product_listing')
def product_listing():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('product_listing.html', products=PRODUCTS)

@app.route('/product_details/<int:product_id>')
def product_details(product_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    product = next((product for product in PRODUCTS if product["id"] == product_id), None)
    if product is None:
        return "Product not found."
    return render_template('product_details.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
