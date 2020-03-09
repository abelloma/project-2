

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
    print("index page")
    return render_template('index.html')

@app.route("/templates/wine.html", method =["POST"])
def wine():
    print("wine page")
    return render_template('/templates/wine.html')

@app.route("/winemap/")
def winemap():

    return render_template('winemap.html')

@app.route("/templates/beermap")
def beermap():

    return render_template('beermap.html')    

@app.route("/API_endpoint", methods=['GET'])
def index():

    data = [("index","state","income","abbr","brewery_count","population","wineries","pct_brewery""pct_winery","per_capita_beer","per_capita_wine","total_breweries","total_wineries")]
    conn = sqlite3.connect('beer_db.sqlite')

    cursor = conn.execute('SELECT * FROM beer;')
    data.append = cursor.fetchall()
    print(data)


    return jsonify(data)

if __name__ == "__main__":
    app.run()