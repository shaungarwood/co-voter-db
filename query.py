#!/usr/bin/env python

import pymongo
from IPython import embed
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["voters"]
mycol = mydb["2019-voters"]

pp = pprint.PrettyPrinter(indent=4)

def search(query):
    res = []
    for x in mycol.find(query): 
        res.append(x.copy())
    return res

def clean_empty(entry):
    for key in list(entry):
        if entry[key] == '':
            del entry[key]

def print_res(res):
    for x in res:
        voter_copy = x.copy()
        clean_empty(voter_copy)
        pp.pprint(voter_copy)

embed()
