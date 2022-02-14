from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_pager():
    return render_template('home.html')
@app.route('/market')

def market_page():
    items =[{'name' : 'Phone', 'id': 1212, 'price' : 1234, 'available': True },
            {'name' : 'Computer', 'id': 3728932, 'price' : 64873, 'available': True },{'name' : 'Router', 'id': 27302, 'price' : 3720983, 'available': False}]

    return render_template('market.html', items=items)
if __name__ == '__main__':
    app.run()
