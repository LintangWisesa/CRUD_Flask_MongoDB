from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import yaml

app = Flask(__name__)
config = yaml.load(open('database.yaml'))
client = MongoClient(config['uri'])
# db = client.lin_flask
db = client['lin_flask']
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        name = body['name']
        age = body['age']

        # db.users.insert_one({
        db['users'].insert_one({
            "name": name,
            "age": age
        })
        return jsonify({
            'status': 'Data is posted to MongoDB!',
            'name': name,
            'age': age
        })
    
    # GET all data from database
    if request.method == 'GET':
        return 'GET'

@app.route('/data/<string:objid>', methods=['GET', 'DELETE', 'PUT'])
def onedata(objid):

    # GET a specific data by id
    if request.method == 'GET':
        return 'GET'
        
    # DELETE a data
    if request.method == 'DELETE':
        return 'DELETE'

    # UPDATE a data by id
    if request.method == 'PUT':
        return 'PUT'

if __name__ == '__main__':
    app.debug = True
    app.run()