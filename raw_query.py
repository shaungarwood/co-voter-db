import pymongo

from IPython import embed

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


client = pymongo.MongoClient(f"mongodb://localhost:27017/")
db = client['voters']

voters = db['2019-voters']
phones = db["phone-nums"]

embed()
