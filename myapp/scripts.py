import pandas as pd


def read_csv():
    df = pd.read_csv("./dsets/automobiles.csv")
    return df


def mpg_cat(mpg):
    if mpg < 15:
        return "Low"
    elif mpg < 25:
        return "Moderate"
    else:
        return "High"


def my_stats(df):
    return df.describe()
