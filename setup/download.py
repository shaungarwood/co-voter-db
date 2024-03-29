#!/usr/bin/env python

import pymongo
from IPython import embed
import csv
from requests import get

from os import remove
import re
import shutil

from zipfile import ZipFile

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["voters"]
# mycol = mydb["2019-voters"]
mycol = mydb["2016-voters"]

part = 1
# url_date = "20191201"
url_date = "20161201"
while True:
    print(f"working on part {part}")
    filename = f"Registered_Voters_List_ Part{part}"
    url = f"http://coloradovoters.info/downloads/{url_date}/{filename}.zip"
    res = get(url)
    if not res.ok:
        print(f"could not download url: {url}")
        break

    with open("downloads/" + filename + ".zip", 'wb') as f:
        f.write(res.content)

    # zip doesn't like spaces in the filename
    newfilename = filename.replace(' ', '')
    shutil.move('downloads/' + filename + ".zip", 'downloads/' + newfilename + ".zip")

    print("  downloaded zip")
    with ZipFile("downloads/" + newfilename + ".zip", 'r') as zipObj:
        zipObj.extractall('downloads/')

    print("  writing to db")
    with open("downloads/" + filename + ".txt", newline='', encoding="ISO-8859-1") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        keys = next(spamreader)
        for row in spamreader:
            voter = zip(keys, row)
            voter = dict(voter)

            for x in voter:
                if voter[x] == '':
                    voter[x] = None

            if voter['PHONE_NUM'] is not None:
                voter['PHONE_NUM'] = re.sub(r'[^\d]', '', voter['PHONE_NUM'])

            if 'MIDDLE_INITIAL' not in voter and voter['MIDDLE_NAME'] is not None:
                if len(voter['MIDDLE_NAME']) == 1:
                    voter['MIDDLE_INITIAL'] = voter['MIDDLE_NAME']
                    voter['MIDDLE_NAME'] = None
                else:
                    voter['MIDDLE_INITIAL'] = voter['MIDDLE_NAME'][0:1]

            mycol.insert_one(voter)

    # remove("downloads/" + filename + ".zip")
    # remove("downloads/" + filename + ".txt")

    print(f"there are {mycol.count_documents({})} records in db")
    print("-"*20)
    part += 1

embed()
