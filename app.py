import datetime as dt
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify#setup database

engine = create_engine("sqlite:///hawaii.sqlite") #create_engine() function allows us to access and query our SQLite database file.
#reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)
print(Base.classes.keys())
session=Session(engine)
Measurement = Base.classes.measurement
Station = Base.classes.station


# build flask route
app = Flask(__name__)  #flask application named "name" is created 
#import app
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#create a precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)






#Create a New Flask App Instance
#app = Flask(__name__)cl
##Create Flask Routes
#@app.route('/')
#def hello_world():
    #return 'Hello world'