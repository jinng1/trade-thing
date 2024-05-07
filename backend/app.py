from flask import Flask, jsonify
from flask_cors import CORS
from binancefutures import get_balance
import config

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/getWalletBalance')
def test():
    balance = get_balance()
    data = {"balance": balance}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)