import re

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['voters']

voters = db['2019-voters']
phones = db["phone-nums"]

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

def dbsearch(query, collection=voters):
    print(collection)
    res = []
    for x in collection.find(query):
        res.append(x.copy())
    [clean_res(x) for x in res]
    return res

def search_name(name):
    first, last = name.split(" ")
    first = first.upper()
    last = last.upper()
    return dbsearch({"FIRST_NAME": first, "LAST_NAME": last})

def search_phone(num):
    num = str(num)
    num = re.sub(r'[^\d]', '', num)
    return dbsearch({"PHONE_NUM": num}, phones)

def clean_res(entry): # i should do this the right way, copy
    for key in list(entry):
        if key in boring_fields or entry[key] == None:
            del entry[key]

def determine_query_type(search_string):
    search_string = search_string.replace('_', ' ')
    if len(re.findall(r'\d', search_string)) >= 10:
        # phone
        return search_phone(search_string)
    elif re.search(r'^\d.+\w', search_string):
        # address
        pass
    elif ' ' in search_string:
        # name
        return search_name(search_string)
    else:
        # unsure
        print("unsure what to do with: ", search_string)
        return []

if __name__ == '__main__':
    import pprint

    from IPython import embed

    pp = pprint.PrettyPrinter(indent=4)

    def print_res(res):
        for x in res:
            voter_copy = x.copy()
            clean_res(voter_copy)
            pp.pprint(voter_copy)

    embed()
