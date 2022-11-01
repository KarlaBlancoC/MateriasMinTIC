from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
def load_file_config():
    with open("config.json") as f:
        data = json.load(f)
    return data

if __name__=="__main__":
    data_config = load_file_config()
    print("Server running: http://{data_config['url-backend']")
    serve(app, host=data_config["url-backend"],port=data_config["port"])