from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
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
        allData = db['users'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            name = data['name']
            age = data['age']
            dataDict = {
                'id': str(id),
                'name': name,
                'age': age
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)

@app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = db['users'].find_one({'_id': ObjectId(id)})
        id = data['_id']
        name = data['name']
        age = data['age']
        dataDict = {
            'id': str(id),
            'name': name,
            'age': age
        }
        print(dataDict)
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        db['users'].delete_many({'_id': ObjectId(id)})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Data id: ' + id + ' is deleted!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        name = body['name']
        age = body['age']

        db['users'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    "name":name,
                    "age":age
                }
            }
        )

        print('\n # Update successful # \n')
        return jsonify({'status': 'Data id: ' + id + ' is updated!'})

if __name__ == '__main__':
    app.debug = True
    app.run()