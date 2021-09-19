# Configuration Tutorial
import json
from pprint import pprint
from mongoengine import *

import pymongo
from flask import Flask, jsonify

app = Flask(__name__)
connect(host="mongodb+srv://jay:jay@learncluster.g5um1.mongodb.net/sample_analytics?retryWrites=true&w=majority")


class airbnb(DynamicDocument):
    # Meta variables.
    meta = {
        'collection': 'customers'
    }


test = airbnb.objects(name="Jennifer Lawrence").first()
print(test.to_json())

all_objects = json.loads(test.to_json())
print(all_objects)
print(type(all_objects))




@app.route('/')
def home():
    return jsonify(all_objects)

app.run(debug=True)
