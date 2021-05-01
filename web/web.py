from flask import Flask, send_from_directory
import requests, json
import os

ROOT_DIR = os.path.dirname(os.path.abspath('.')) + '/books'

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<filename>')
def sendFiles(filename):
    return send_from_directory(ROOT_DIR + '/src/', filename + '.txt')

@app.route('/pair/<word>')
def getPair(word):
    return 'chuj'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)