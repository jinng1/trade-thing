from flask import Flask, jsonify
from flask_cors import CORS
import config
import os
from utils.mongodb import MongoDBManager
from utils.binancefutures import get_balance, get_tickers, get_positions

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
CORS(app)

db_manager = MongoDBManager(app.config)

@app.route('/getWalletBalance')
def getWalletBalance():
    balance = get_balance()
    data = {"balance": balance}
    return jsonify(data)

@app.route('/getTickers')
def getTickers():
    tickers = get_tickers()
    data = {"tickers": tickers}
    print(tickers)
    return jsonify(data)

@app.route('/getPositions')
def getPositions():
    positions = get_positions()
    data = {"positions": positions}
    print(positions)
    return jsonify(data)

# @app.route('/addTrade')
# def addTrade():
#     MongoDBManager.add_to_collection()

if __name__ == '__main__':
    app.run(debug=True)