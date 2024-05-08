from flask import Flask, jsonify
from flask_cors import CORS
import config
import os
from utils.mongodb import MongoDBManager
from utils.binancefutures import get_balance

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
CORS(app)

db_manager = MongoDBManager(app.config)

@app.route('/getWalletBalance')
def getWalletBalance():
    balance = get_balance()
    data = {"balance": balance}
    return jsonify(data)

@app.route('/pingdb')
def pingdb():
    try:
        db_manager.ping() # Test basic connection
        return jsonify({'message': 'Connection successful!'})
    except Exception as e:
        return jsonify({'message': f'Connection error: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)