"""
Dylan Pool
Section AE
Final Project
This file uses pandas dataframes to create a Decision Tree model and find
The features that contribute most to certain labels.
"""


import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from team_stats_prep_data import open_files
from cse163_utils import assert_equals


def machine_learning(df1, df2, lab):
    """
    This method creates an ExtraTreesRegressor model, fitting features and
    labels from the two dataframes given. The model calculates the feature
    importance for both dataframes and returns a tuple of a list
    of the scores from the feature importance.
    """
    features1 = df1.loc[:, df1.columns != lab]
    features2 = df2.loc[:, df2.columns != lab]
    label1 = df1[lab]
    label2 = df2[lab]
    model = ExtraTreesRegressor(random_state=0)

    model.fit(features1, label1)
    scores1 = model.feature_importances_
    scores1 = np.around(scores1 * 100, decimals=2)
    assert_equals(np.ndarray, type(scores1))

    model.fit(features2, label2)
    scores2 = model.feature_importances_
    scores2 = np.around(scores2 * 100, decimals=2)

    return scores1, scores2


def results(s1, s2, df):
    """
    This method prints the scores given, breaking each stat up onto it's own
    line, and printing each decades score side by side.
    """
    count = 0
    columns = df.columns[1:]
    print('Percentage of each statistic\'s importance to ' +
          df.columns[0] + ':')
    print('Decade: 2000\'s  2010\'s')
    for column in columns:
        print(column + ':    ' + str(s1[count]) + '     ' + str(s2[count]))
        count += 1


def main():
    """
    This method runs all of the other methods.
    """
    df_00, df_10 = open_files('/home/team_stats/')
    assert_equals(0.752, df_00.iloc[3, 7])  # Same test as in prep_data
    scores_00, scores_10 = machine_learning(df_00, df_10, 'PTS')
    results(scores_00, scores_10, df_00)


if __name__ == '__main__':
    main()
