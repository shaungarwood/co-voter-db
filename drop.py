#!/usr/bin/env python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["voters"]
mycol = mydb["2019-voters"]

print(mycol.count_documents({})
mycol.drop()
print(mycol.count_documents({})
