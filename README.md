# sqlalchemy
 
This repo contains data exploration and analysis on Hawaii's climate. It analyzes precipitation and temperature data on different time series.

# Data Sources
- Resources dir contains all data files.
- It includes hawaii.sqlite file and csvs

# Climate Analysis
- It includes reflection of database using hawaii.sqlite file.
- Calculate the total number of stations in the dataset
- Find the most active stations (i.e. which stations have the most rows?).
    - List the stations and observation counts in descending order.
    - Which station id has the highest number of observations?
    - Using the most active station id, calculate the lowest, highest, and average temperature.
- Retrieve the last 12 months of temperature observation data (TOBS).
    - Filter by the station with the highest number of observations.
    - Query the last 12 months of temperature observation data for this station.

# Flask API
Designed Flask API based on queries developed for climate anylsis above. Following routes are created:
- /
  - Home page and provides all routes that are available.

- /api/v1.0/precipitation
  - Convert the query results to a dictionary using date as the key and prcp as the value.
  - Return the JSON representation of your dictionary.

- /api/v1.0/stations
  - Return a JSON list of stations from the dataset.

- /api/v1.0/tobs
  - Query the dates and temperature observations of the most active station for the last year of data.
  - Return a JSON list of temperature observations (TOBS) for the previous year.

- /api/v1.0/<start> and /api/v1.0/<start>/<end>
  - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

# Temperature Analysis
- Identify the average temperature in June at all stations across all available years in the dataset. Same for December temperature.
- Use the t-test to determine whether the difference in the means, if any, is statistically significant.
- Use the calc_temps function to calculate the min, avg, and max temperatures for trip using the matching dates from a previous year (i.e., use “2017-08-01”).
- Plot the min, avg, and max temperature from your previous query as a bar chart.

# Daily Rainfall Average
- Calculate the rainfall per weather station using the previous year’s matching dates.
  - Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.
- Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
- Load the list of daily normals into a Pandas DataFrame.
- Use Pandas to plot an area plot (stacked=False) for the daily normals.


