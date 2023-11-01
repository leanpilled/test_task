import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ.get('MONGO_URI'))
db = client.mydatabase
collection = db.key_value_store
    
@app.get('/key_value')
def get_value():
    key = request.args.get('key')
    value = collection.find_one({"key": key})
    if value:
        return jsonify({"key": key, "value": value["value"]}), 200
    return jsonify({"error": "Key not found"}), 404

@app.post('/key_value')
def post_value():
    key = request.form['key']
    value = request.form['value']
    if key and value:
        collection.insert_one({"key": key, "value": value})
        return jsonify({"message": "Key-Value pair created"}), 201
    return jsonify({"error": "Invalid request data"}), 400

@app.put('/key_value')
def update_value():
    key = request.form['key']
    value = request.form['value']
    if key and value and collection.find_one({"key": key}):
        collection.update_one({"key": key}, {"$set": {"value": value}})
        return jsonify({"message": "Key-Value pair updated"}), 200
    return jsonify({"error": "Invalid request data"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
