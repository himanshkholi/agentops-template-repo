from flask import Flask, jsonify
import json

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Welcome to Barbeque Nation API! Use /restaurants or /faqs to get data."

# JSON file read karo
with open('apis/knowledge_base.json', 'r') as file:
    data = json.load(file)

# Restaurants ke liye API endpoint
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(data['restaurants'])

# FAQs ke liye API endpoint
@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(data['faqs'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)