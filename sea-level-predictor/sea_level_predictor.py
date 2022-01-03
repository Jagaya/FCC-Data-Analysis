import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv",
                     index_col="Year",
                     float_precision='legacy')
    x1 = df.index
    y = df["CSIRO Adjusted Sea Level"]#.astype(np.float16)
    fig = plt.subplots(figsize=(7, 5))

    # Create scatter plot
    plt.scatter(x=x1, y=y)

    # Create first line of best fit
    res = linregress(x1, y)
    plt.plot(range(1880, 2050),
             res.intercept + res.slope * range(1880, 2050),
             'g',
             label='fitted line')

    # Create second line of best fit
    res2 = linregress(x1[x1 >= 2000], y[x1 >= 2000])
    plt.plot(range(2000, 2050),
             res2.intercept + res2.slope * range(2000, 2050),
             "r",
             label="prediction")

    # Add labels and title
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("Sea Level (inches)", fontsize=15)
    plt.title("Rise in Sea Level", fontsize=14)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
