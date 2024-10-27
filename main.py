from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    products = [
        {'name': 'Phone', 'price': 299.99, 'image': 'phone.png'},
        {'name': 'Headphones', 'price': 99.99, 'image': 'headphones.png'},
        {'name': 'Red Moon', 'price': 299.99, 'image': 'red_moon.png'},  # New product
        {'name': 'Diamond Grill', 'price': 499.99, 'image': 'diamond_grill.png'},  # New product
        {'name': "DOOM's Sword", 'price': 599.99, 'image': 'sword.png'},  # New product
        {'name': 'Light Bulb For Thoughts', 'price': 29.99, 'image': 'Lightbulb.png'}  # New Product
    ]
    return render_template('index.html', products=products)


@app.route('/payment')
def payment():
    item_name = request.args.get('item')
    amount = request.args.get('price')
    return render_template('payment.html', item_name=item_name, amount=amount)


if __name__ == '__main__':
    app.run(debug=True)
