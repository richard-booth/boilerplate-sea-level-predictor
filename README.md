# Assignment: Sea Level Predictor
This assignment provides a data set on sea level measurements by year from 1880-2013. The task is to make a scatter plot of the data, and add two linear regression lines that illustrate how sea levels might rise up to 2050 if trends continue. The first (red) line is based on the whole 1880-2013 trend, and extends it to 2050. The second (blue) line is based on the trend from 2000-2013, and extends it to 2050.

See the [notebook](https://github.com/richard-booth/sea-level-predictor/blob/main/sea_level_predictor.ipynb) (`sea_level_predictor.ipynb`) for a walk-through of my solution, which is contained in `sea_level_predictor.py`.

## Instructions:

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

- Use Pandas to import the data from epa-sea-level.csv.
- Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
- Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
- Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
- The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.

Development
Write your code in sea_level_predictor.py. For development, you can use main.py to test your code.
