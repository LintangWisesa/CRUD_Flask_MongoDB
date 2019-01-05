from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import yaml

app = Flask(__name__)
config = yaml.load(open('database.yaml'))
client = MongoClient(config['uri'])
db = client.lin_flask
# db = client['lin_flask']
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()