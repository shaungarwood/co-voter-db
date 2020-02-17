#!/usr/bin/env python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["voters"]
mycol = mydb["phone-nums"]

print(mycol.count_documents({}))
mycol.drop()
print(mycol.count_documents({}))
