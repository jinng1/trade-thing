from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/getWalletBalance')
def test():
    data = {"balance": 333}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)