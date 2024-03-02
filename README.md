# Data Analysis Using SQLAlchemy

## Background
For this challenge, I decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I need to take to accomplish this task.

## Part 1: Analyzing and Exploring the Climate Data
In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of my climate database. Specifically, I utilized SQLAlchemy Object Relational Mapper queries, Pandas, and Matplotlib. I used the provided hawaii.sqlite database to store the data and climate-analysis.ipynb to complete my climate analysis. Using these files, I completed the following steps:

1. Used the SQLAlchemy create_engine() function to connect to your SQLite database.
2. Used the SQLAlchemy automap_base() function to reflect your tables into classes, and then saved references to the classes named station and measurement.
3. Linked Python to the database by creating a SQLAlchemy session.

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/302073f6-d121-498b-a13f-bab8bb0031e7)

**Figure 1.** *Importing dependencies, creating the engine, reflecting the tables, creating a session, and saving the measurement and station information into variables*


### Precipitation Analysis
I performed a precipitation analysis by completing the steps.

1. Found the most recent date in the dataset.
2. Using that date, I obtained the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Selected only the "date" and "prcp" values.
4. Loaded the query results into a Pandas DataFrame. I explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method, as the following image shows:

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/004b3d57-db7a-4115-a0ca-14af2030ea4f)

**Figure 2.** *Bar graph of montly precipitation data.*

7. Use Pandas to print the summary statistics for the precipitation data.

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/8dbc4946-6c16-4e0c-9f65-693c97de88c2)

**Figure 2.** *Bar graph of montly precipitation data.*

### Station Analysis
I performed a station analysis by completing the steps:

1. Designed a query to calculate the total number of stations in the dataset.
2. Designed a query to find the most-active stations (that is, the stations that have the most rows). To do so, I completed the following steps:
    * Listed the stations and observation counts in descending order.
    * The station id with the greatest number of observations is *USC00519281*
3. Designed a query that calculates the lowest, highest, and average temperatures for station *USC00519281*.
4. Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, I completed the following steps:
    * Filtered by the station that has the greatest number of observations.
    * Queried the previous 12 months of TOBS data for that station.
    * Plotted the results as a histogram with bins=12, as the following image shows:

5. Closed my session.



## Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

/

Start at the homepage.

List all the available routes.

/api/v1.0/precipitation

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

/api/v1.0/stations

Return a JSON list of stations from the dataset.
/api/v1.0/tobs

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
