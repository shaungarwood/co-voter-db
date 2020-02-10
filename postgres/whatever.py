#!/usr/bin/env python

from IPython import embed
import psycopg2

connect_str = "dbname='voters' user='voter' host='localhost' " + \
              "password=colorado"
conn = psycopg2.connect(connect_str)

cursor = conn.cursor()
cursor.execute("""CREATE TABLE voter_list (name char(40));""")
CREATE TABLE persons
(
  id serial NOT NULL,
  first_name character varying(50),
  last_name character varying(50),
  dob date,
  email character varying(255),
  CONSTRAINT persons_pkey PRIMARY KEY (id)
)

"VOTER_ID","COUNTY_CODE","COUNTY","LAST_NAME","FIRST_NAME","MIDDLE_NAME","NAME_SUFFIX","VOTER_NAME","STATUS_CODE","PRECINCT_NAME","ADDRESS_LIBRARY_ID","HOUSE_NUM","HOUSE_SUFFIX","PRE_DIR","STREET_NAME","STREET_TYPE","POST_DIR","UNIT_TYPE","UNIT_NUM","RESIDENTIAL_ADDRESS","RESIDENTIAL_CITY","RESIDENTIAL_STATE","RESIDENTIAL_ZIP_CODE","RESIDENTIAL_ZIP_PLUS","EFFECTIVE_DATE","REGISTRATION_DATE","STATUS","STATUS_REASON","BIRTH_YEAR","GENDER","PRECINCT","SPLIT","VOTER_STATUS_ID","PARTY","PREFERENCE","PARTY_AFFILIATION_DATE","PHONE_NUM","MAIL_ADDR1","MAIL_ADDR2","MAIL_ADDR3","MAILING_CITY","MAILING_STATE","MAILING_ZIP_CODE","MAILING_ZIP_PLUS","MAILING_COUNTRY","SPL_ID","PERMANENT_MAIL_IN_VOTER","CONGRESSIONAL","STATE_SENATE","STATE_HOUSE","ID_REQUIRED"

cursor.execute("""SELECT * from voter_list""")

rows = cursor.fetchall()
print(rows)

embed()

cursor.close()
conn.close()
