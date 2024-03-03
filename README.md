# Data Analysis Using SQLAlchemy

## Background
For this challenge, I decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I need to take to accomplish this task.

## Part 1: Analyzing and Exploring the Climate Data
In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of my climate database. Specifically, I utilized SQLAlchemy Object Relational Mapper queries, Pandas, and Matplotlib. I used the provided hawaii.sqlite database to store the data and climate-analysis.ipynb to complete my climate analysis. Using these files, I completed the following steps:

1. Used the SQLAlchemy create_engine() function to connect to my SQLite database.
2. Used the SQLAlchemy automap_base() function to reflect my tables into classes, and then saved references to the classes named station and measurement.
3. Linked Python to the database by creating a SQLAlchemy session.

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/302073f6-d121-498b-a13f-bab8bb0031e7)

**Figure 1.** *Importing dependencies, creating the engine, reflecting the tables, creating a session, and saving the measurement and station information into variables*

## Precipitation Analysis
I performed a precipitation analysis by completing the steps.

1. Found the most recent date in the dataset.
2. Using that date, I obtained the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Selected only the "date" and "prcp" values.
4. Loaded the query results into a Pandas DataFrame. I explicitly set the column names.
5. Sorted the DataFrame values by "date".
6. Plotted the results by using the DataFrame plot method, as the following image shows:

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/978ec827-a895-4a7b-8ddd-e25206cacf9f)

**Figure 2.** *Bar graph of montly precipitation data.*

7. Use Pandas to print the summary statistics for the precipitation data.

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/8dbc4946-6c16-4e0c-9f65-693c97de88c2)

**Figure 2.** *Summary statistics of precipitation data.*

## Station Analysis
I performed a station analysis by completing the steps:

1. Designed a query to calculate the total number of stations in the dataset.
2. Designed a query to find the most-active stations (that is, the stations that have the most rows). To do so, I completed the following steps:
    * Listed the stations and observation counts in descending order.
    * The station id with the greatest number of observations is *USC00519281*
3. Designed a query that calculates the lowest, highest, and average temperatures for station *USC00519281* (the most-active station).

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/0dd83ac7-c787-4b81-8f04-19648de23b70)

**Figure 3.** *Queries to locate the most-active station and the lowest, highest, and average temperatures for the most-active station.*

4. Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, I completed the following steps:
    * Filtered by the station that has the greatest number of observations.
    * Queried the previous 12 months of TOBS data for that station.
    * Plotted the results as a histogram with bins=12, as the following image shows:

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/a0429b37-fa2a-4eab-95c6-a16c3eaac531)

**Figure 4.** *Bar Graph of the frequency of each temperature for the most-active station.*

5. Closed my session.

## Part 2: Climate App Using Flask
After I completed my climate analysis in jupyter, I designed a Flask API based on the queries that I just developed above. To do so, I used Flask to create my routes as follows:

**Route 1:** Homepage
* Start at the homepage.
* Lists all the available routes.

**Route 2:** /api/v1.0/precipitation
* Converts the query results from my precipitation analysis (i.e. retrieve only the last 12 months of precipitation data) to a dictionary using date as the key and prcp as the value.
* Returns the JSON representation of my dictionary.
    
**Route 3:** /api/v1.0/stations
* Returns a JSON list of stations from the dataset.

**Route 4:** /api/v1.0/tobs
* Queries the dates and temperature observations of the most-active station for the previous year of data.
* Returns a JSON list of temperature observations for the previous year.

**Route 5:** /api/v1.0/\<start> and /api/v1.0/\<start>/\<end>
* Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
* For a specified start, the max, min, and average temperature will be calculated for all the dates greater than or equal to the start date.
* For a specified start date and end date, the max, min, and average temperature will be calculated for the dates from the start date to the end date, inclusive.

![image](https://github.com/nicholaishaw/sqlalchemy-challenge/assets/135463220/40d9a078-04dc-4274-86f3-c3a8278c9754)

**Figure 5.** *A sample route in the Flask app: minimum, maximum, and average temperature data greater than or equal to the date provided by the user or minimum, maximum, and average temperature data between the dates provided by the user, inclusive. Full Flask app is located in the 'app.py' file in this repository.*
