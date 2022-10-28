import pymongo
from flask import request
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['test-database']
collection = db['test']
from flask import Flask

app = Flask(__name__)
@app.route('/login', methods=['POST'])

def login():
    var={"name":"John", "age":30, "car":null}
    test = db.test
    post_id = posts.insert_one(var).inserted_id
    find=db.test.find({})
    return json_utils.dumps(find)
if __name__ == '__main__':
    app.run(debug=True)
