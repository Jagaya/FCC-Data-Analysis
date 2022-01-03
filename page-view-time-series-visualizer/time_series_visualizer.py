import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[(df.value >= df.value.quantile(0.025))
        & (df.value <= df.value.quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.subplots(figsize=(10, 3))

    fig = sns.lineplot(x=df.index, y=df["value"], color="red")

    fig.set(xlabel='Date',
            ylabel='Page Views',
            title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    fig = fig.figure
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year", "month"]).value.mean().reset_index()

    months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]
    df_bar["month"] = df_bar["month"].apply(lambda x: months[x - 1])

    # Draw bar plot
    fig = plt.subplots(figsize=(10, 6))

    fig = sns.barplot(data=df_bar,
                      x="year",
                      y="value",
                      hue="month",
                      hue_order=months)

    fig.set(xlabel='Years', ylabel='Average Page Views')

    fig = fig.figure
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Copy and modify data for monthly bar plot
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.month

    months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    df_box["month"] = df_box["month"].apply(lambda x: months[x - 1])

    # Draw box plot (using Seaborn)
    fig, ax = plt.subplots(figsize=(11, 7), ncols=2)

    fig1 = sns.boxplot( data = df_box,
                        x = 'year',
                        y ='value',
                        ax= ax[0]
                        )
    fig1.set(xlabel='Year', ylabel='Page Views', title = "Year-wise Box Plot (Trend)")

    fig2= sns.boxplot( data=df_box,
                       x='month', 
                       y ='value',
                       ax= ax[1],
                       order = months
                       )
    fig2.set(xlabel= 'Month', ylabel = 'Page Views',title = "Month-wise Box Plot (Seasonality)")

    #fig = fig.figure
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig