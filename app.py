

from flask import Flask, render_template, jsonify, after_this_request
# from flask_pymongo import PyMongo
import sqlalchemy
import sqlite3
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json

app = Flask(__name__)
# SQLAlchemy Setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)

Base = automap_base()

Base.prepare(db.engine, reflect=True)



@app.route("/")
def api_call():

    return render_template('index.html')

@app.route("/API_endpoint", methods=['GET'])
def index():
    # singledocument = mongo.db.fruits_db.find({})
    # states = []
    # for x in singledocument:
    #     data.append({'vendor' : x['vendor'], 'fruit' : x['fruit'], 'quantity' : x['quantity']})

    # return jsonify(data)
    conn = sqlite3.connect('db.sqlite')

    cursor = conn.execute('SELECT * FROM beer;')
    data = cursor.fetchall()
    print(data)
    # print (data( json_str = True ))
    # row_json = json.dumps(data)
    # print(row_json)

    # for row in data:
    #     print(row)
    #     states.append(row)

    return jsonify(data)

if __name__ == "__main__":
    app.run()