from flask import Flask, request, flash, redirect, url_for, jsonify
from flask_cors import CORS,cross_origin
import requests

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def index():        

    body = request.get_json()
    print(body['token'])
    data = {'msg':"Successfully attacked"}
    return jsonify(data)



if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )