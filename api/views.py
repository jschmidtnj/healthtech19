from run import app
from flask import jsonify


@app.route('/hello')
def index():
    return jsonify({'message': 'Hello, World!'})
