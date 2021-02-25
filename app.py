import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime
from sqlalchemy import desc
import pandas as pd
from flask import Response

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and precipitation"""
    # Query all dates and precipitation
    
    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()
    
    all_dates_prcp=[]
    
    for date,prcp in results:
        date_dict = {}
        date_dict['date']=date
        date_dict['prcp']=prcp
        all_dates_prcp.append(date_dict)

    return jsonify(all_dates_prcp)


@app.route("/api/v1.0/stations")
def stations():
    
#     Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
#     Query all stations
    results = session.query(Station.name, Station.station).order_by(Station.name).all()

    session.close()
    
    all_stations=[]
    
    for name, station in results:
        station_dict = {}
        station_dict['name']=name
        station_dict['station']=station
        all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
   
#     Create our session (link) from Python to the DB
    session = Session(engine)

#     Find the most recent date in the data set.
    most_recent_date = session.query(func.max(Measurement.date)).one()
    most_recent_date = most_recent_date[0]

#     Calculate the date one year from the last date in data set.
    last_year_date = datetime.strptime(most_recent_date, "%Y-%m-%d") + relativedelta(years=-1)
    last_year_date

#     Query for the dates and temperature observations of the most active station for the last year of data
    station_list = session.query(Measurement.station,func.count(Measurement.station).label('station count')).\
                group_by(Measurement.station).\
                order_by(desc('station count')).all()
    
    most_active_station_id = station_list[0][0]
    
    temp_observation_data = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == most_active_station_id).order_by(Measurement.date).\
    filter(Measurement.date <= most_recent_date).\
    filter(Measurement.date >= last_year_date)

    session.close()
    
    all_tobs_for_last_year=[]
    
    for date, tobs in temp_observation_data:
        tobs_dict = {}
        tobs_dict['date']=date
        tobs_dict['tobs']=tobs
        all_tobs_for_last_year.append(tobs_dict)

    return jsonify(all_tobs_for_last_year)


if __name__ == '__main__':
    app.run(debug=True)
