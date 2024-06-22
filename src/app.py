from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)

API_BASE_URL = 'https://apiv3.imocha.io/v3'
MOCHA_API_KEY = 'API KEY'

if __name__ == '__main__':
    app.run(debug=True, port=4000)


