#!/usr/bin/env python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["voters"]
mycol = mydb["2019-voters"]

phone_col = mydb["phone-nums"]

interesting_keys = [
    'VOTER_ID',
    'LAST_NAME',
    'FIRST_NAME'
]

voters = mycol.find({"PHONE_NUM": {"$ne": ''}})
for voter in voters:
   contact = {"PHONE_NUM": voter["PHONE_NUM"]}
   for key in interesting_keys:
       if key in voter:
           contact[key] = voter[key]

   phone_col.insert_one(contact)
