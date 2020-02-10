#!/usr/bin/env python

import pymongo
from IPython import embed
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["voters"]
mycol = mydb["2019-voters"]

pp = pprint.PrettyPrinter(indent=4)

boring_fields = [
    "ADDRESS_LIBRARY_ID",
    "CONGRESSIONAL",
    "COUNTY_CODE",
    "HOUSE_NUM",
    "ID_REQUIRED",
    "PERMANENT_MAIL_IN_VOTER",
    "PRE_DIR",
    "PRECINCT",
    "PRECINCT_NAME",
    "SPLIT",
    "SPL_ID",
    "STATE_HOUSE",
    "STATE_SENATE",
    "STATUS_CODE",
    "STREET_NAME",
    "STREET_TYPE",
    "VOTER_STATUS_ID",
    "_id"
]

def search(query):
    res = []
    for x in mycol.find(query): 
        res.append(x.copy())
    [clean_res[x] for x in res]
    return res

def search_name(name):
    first, last = name.split(" ")
    return search({"FIRST_NAME": first, "LAST_NAME": last})

def clean_res(entry):
    for key in list(entry):
        if key in boring_fields or entry[key] == '':
            del entry[key]

def print_res(res):
    for x in res:
        voter_copy = x.copy()
        clean_res(voter_copy)
        pp.pprint(voter_copy)

embed()
