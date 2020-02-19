import re

import pymongo

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


class VoterRecords:
    def __init__(self, db="localhost", port="27017"):
        client = pymongo.MongoClient(f"mongodb://{db}:{port}/")
        db = client['voters']

        self._col_voters = db['2019-voters']
        self._col_phones = db["phone-nums"]

    def dbsearch(self, query, collection='voters'):
        res = []
        if collection == 'voters':
            for x in self._col_voters.find(query):
                res.append(x.copy())
        elif collection == 'phones':
            for x in self._col_phones.find(query):
                res.append(x.copy())

        [self.clean_res(x) for x in res]
        return res

    def search_name(self, name):
        search = {}
        name = name.upper().split(" ")
        if len(name) == 3:
            if len(name[1]) == 1:
                search['MIDDLE_INITIAL'] = name.pop(1)
            else:
                search['MIDDLE_NAME'] = name.pop(1)
        search['LAST_NAME'] = name.pop()
        search['FIRST_NAME'] = name.pop()

        return self.dbsearch(search)

    def search_phone(self, num):
        num = str(num)
        num = re.sub(r'[^\d]', '', num)
        return self.dbsearch({"PHONE_NUM": num}, 'phones')

    def clean_res(self, entry):  # i should do this the right way, copy
        for key in list(entry):
            if key in boring_fields or entry[key] is None:
                del entry[key]

    def determine_query_type(self, search_string):
        search_string = search_string.replace('_', ' ')
        if len(re.findall(r'\d', search_string)) >= 10:
            # phone
            return self.search_phone(search_string)
        elif re.search(r'^\d.+\w', search_string):
            # address
            pass
        elif ' ' in search_string:
            # name
            return self.search_name(search_string)
        else:
            # unsure
            print("unsure what to do with: ", search_string)
            return []


if __name__ == '__main__':
    import pprint

    from IPython import embed

    pp = pprint.PrettyPrinter(indent=4)

    vr = VoterRecords(db="localhost")

    def print_res(res):
        for x in res:
            voter_copy = x.copy()
            vr.clean_res(voter_copy)
            pp.pprint(voter_copy)

    embed()
