import re
import json
import pymongo

from flask import Flask
from flask import request

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['voters']

collection = db['2019-voters']

def search(query):
    res = []
    for x in collection.find(query):
        res.append(x.copy())
    [clean_res(x) for x in res]
    return res

def search_name(name):
    first, last = name.split(" ")
    first = first.upper()
    last = last.upper()
    return search({"FIRST_NAME": first, "LAST_NAME": last})

def search_phone(num):
    num = str(num)
    num = re.sub(r'[^\d]', '', num)
    return search({"PHONE_NUM": num})

def clean_res(entry): # i should do this the right way, copy
    for key in list(entry):
        if key in boring_fields or entry[key] == None:
            del entry[key]

@app.route('/search')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

if __name__ == '__main__':
    app.run()
