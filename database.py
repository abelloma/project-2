import pymongo 
import os
import pandas as pd
import csv
from sqlalchemy import create_engine

combined_data = 'data/combined_data.csv'

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.beer_db
collection = db.states

# def csv_to_dict():
#     reader = csv.DictReader(open(combined_data))
#     result = {}
#     for row in reader:
#         key = row.pop('First_value')
#         result[key] = row
#     return query

# # Final insert statement
# db.collection.insert_one(csv_to_dict())

def csv_to_json(filename, header=none):
    data = pd.read_csv(filename, header=header)
    return data.to_dict('records')

collection.insert_many(csv_to_json(combined_data))
