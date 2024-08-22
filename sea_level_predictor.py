import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    
    fig = df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level').figure

    plt.title('')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    
    # Create first line of best fit
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xtnd1 = pd.Series(list(range(1880, 2051)))
    plt.plot(xtnd1, res1.intercept + res1.slope* xtnd1, 'r')

    # Create second line of best fit
    df_recent = df[df['Year']>=2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    xtnd2 = pd.Series(list(range(2000, 2051)))
    plt.plot(xtnd2, res2.intercept + res2.slope* xtnd2, 'b')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

