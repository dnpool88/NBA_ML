"""
Dylan Pool
Section AE
Final Project
This file reads in a folder containing csv files and creates
multiple pandas dataframes with the cleaned data from the csv files.
"""

import pandas as pd
import os
from cse163_utils import assert_equals


def open_files(folder):
    """
    This method opens the folder of csv files containing team stats, and
    creates 2 pandas dataframes containing the cleaned data for each decade.
    Returns a tuple of dataframes
    """
    df_decades = {}
    files = os.listdir(folder)
    sorted_files = sorted(files)

    for filename in sorted_files:
        full = os.path.join(folder, filename)
        df = pd.read_csv(full)
        df_new = clean_data(df)
        df_decades[filename] = df_new

    df_decades = pd.concat(df_decades.values())

    df_00 = df_decades.iloc[:10, :]
    df_10 = df_decades.iloc[10:, :]
    assert_equals(10, len(df_00.index))
    assert_equals(10, len(df_10.index))
    assert_equals(0.752, df_00.iloc[3, 7])

    return df_00, df_10


def clean_data(df):
    """
    This method takes a dataframe and cleans it down to just the league avg
    stats that impact scoring, returning the cleaned dataframe.
    """
    df = df[df['Team'] == 'League Average']
    df = df[['PTS', 'AST', '2PA', '3PA', 'ORB', 'STL', 'FTA', 'FT%', 'TOV']]
    assert_equals(9, len(df.columns))
    assert_equals(1, len(df.index))
    return df


def main():
    """
    This method runs the other two methods.
    """
    df_00, df_10 = open_files('/home/team_stats/')


if __name__ == '__main__':
    main()
