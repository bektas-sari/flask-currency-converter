import os
import requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# API Key and Base URL
API_KEY = os.getenv("API_KEY")
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    # Validate input parameters
    if not from_currency or not to_currency or not amount:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        amount = float(amount)
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

    # Fetch exchange rate data
    response = requests.get(BASE_URL + from_currency)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch exchange rate"}), 500

    data = response.json()
    if to_currency not in data["conversion_rates"]:
        return jsonify({"error": "Invalid currency code"}), 400

    exchange_rate = data["conversion_rates"][to_currency]
    converted_amount = amount * exchange_rate

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted_amount": round(converted_amount, 2),
        "exchange_rate": exchange_rate
    })

if __name__ == '__main__':
    app.run(debug=True)
