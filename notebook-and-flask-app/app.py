# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd
import datetime as dt


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#This route accesses the homepage
@app.route("/")
def homepage():
    
    #This will return a list of the available routes in the browser page
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/yyyy-mm-dd<br/>"
        f"/api/v1.0/temp/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )

#This route returns the precitipation data from the period 08-23-2016 to 08-23-2017 
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    # Obtain the date a year from 8-23-2017 (the last date in the database)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    print("Query Date: ", query_date)

    # Perform a query to retrieve the data and precipitation scores from the query date (above; line 65) until the final date in the dataset (8-23-2017)
    sql_variable = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= query_date).\
    order_by(measurement.date).all()
    precip = {}

    # Store the date and precipitation in a dictionary
    for date, prcp in sql_variable:
         precip[date]=prcp

    session.close()

    # Return the data in JSON format
    return jsonify(precip)

#This route returns a list of stations in the database
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # Query to calculate the total number of stations in the dataset
    station_all = session.query(station.station).all()
    session.close()

    # Return the list in the browser
    station_list = list(np.ravel(station_all))
    return jsonify(stations = station_list)

#This route returns the dates and temperatures for the most-active stations from the last year of data (8-23-2016 until 8-23-2017)
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    #Obtain the date period and query the temperature and station name for the date period
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_all = session.query(measurement.tobs).filter(measurement.station == "USC00519281").filter(measurement.date >= query_date).all()

    session.close()

    #Return the JSON list in the browser
    temp_list = list(np.ravel(tobs_all))
    return jsonify(tobs = temp_list)

#These routes return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    session = Session(engine)
    
    #Select the dates and query the minimum, average, and maximum temperatures for each date greater than the start date provided by the user, inclusive
    sel = [measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
    
    if not end:
        results = session.query(*sel).filter(measurement.date >= start).group_by(measurement.date).all()
    
    #Select the dates and query the minimum, average, and maximum temperatures for each date greater than the start date and less than the end date provided by the user, inclusive
    else:
        results = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).group_by(measurement.date).all()

    session.close()

    #Create a list to store temperature statistics for each date
    temp_stats_list = []

    #Loop through the results and create a dictionary for each date
    for date, min_temp, avg_temp, max_temp in results:
        temp_stats_dict = {
            "Date": date,
            "Minimum Temperature": min_temp,
            "Average Temperature": avg_temp,
            "Maximum Temperature": max_temp
        }
        temp_stats_list.append(temp_stats_dict)

    #Return the list in the browser
    return jsonify(temp_stats_list)

if __name__ == "__main__":
    app.run(debug=True)