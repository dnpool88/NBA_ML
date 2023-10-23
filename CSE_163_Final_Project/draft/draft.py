"""
Thomas Wilson
Section AE
Final Project
Performing neccesary data wrangling to answer the question:
"From the two decades since 2000, which decade has had better draft class?"
"""

import pandas as pd
from draft_wrangle import read_and_edit

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def one_seasoners(data):
    """
    calculate which decade had more people who played <= 1 season (82 games)
    returns dataframe with those people.
    """
    # make NA's 0 (they never played a game)
    data['G'] = data['G'].fillna(0)
    # transform all strings to NA. need to remove them to do more wrangling.
    data['G'] = pd.to_numeric(data['G'], errors='coerce')

    # find those who played <= 1 season
    busts = data['G'] <= 82
    # remove duplicates
    return(data[busts].drop_duplicates(subset=['Player']))


def mpg(data, range1, range2):
    """
    returns dataset full of NBA players who had <10 mpg per game
    takes in data
    takes in desired MPG to filter by
    returns dataframe with people inbetween that data range
    """
    # make NA's 0 (they never played a game)
    data['MP.1'] = data['MP.1'].fillna(0)
    # transform all strings to NA. need to remove them to do more wrangling.
    data['MP.1'] = pd.to_numeric(data['MP.1'], errors='coerce')
    # get user inputted mpg
    mpg2 = data['MP.1'] > range1
    mpg1 = data['MP.1'] < range2
    return(data[mpg1 & mpg2].drop_duplicates(subset=['Player']))


def main():
    # call data
    df2010, df2000 = read_and_edit()

    # checking how updated data is, comparing these stats to NBA.com stats
    # https://www.nba.com/stats/player/2544/career?PerMode=Totals
    # draft_2003 = df2000[df2000['year'] == 2003]
    # lebron = draft_2003[draft_2003['Player'] == "LeBron James"]

    # Does Lebron have 1354 games played?
    # check_approx_equals("1354", lebron['G'])

    # Does Lebron have 51673 minutes played?
    # check_approx_equals("51673", lebron['MP'])

    # get people who haven't played more than 82 games
    one_season_2000 = one_seasoners(df2000)
    one_season_2010 = one_seasoners(df2010)

    # is leBron in the dataset? he shouldn't be.
    # test_lebron = one_season_2000
    # [one_season_2000['Player'] == "LeBron James"]
    # print(test_lebron)

    # make dataset with the removal of those players
    new_set_2000 = (pd.merge(df2000, one_season_2000,
                             indicator=True, how='outer')
                    .query('_merge=="left_only"')
                    .drop('_merge', axis=1))

    new_set_2010 = (pd.merge(df2010, one_season_2010,
                             indicator=True, how='outer')
                    .query('_merge=="left_only"')
                    .drop('_merge', axis=1))

    # for those who have played more than 82 games, get <10 mpg players
    mpg0_2010 = mpg(new_set_2010, 0, 10)
    mpg0_2000 = mpg(new_set_2000, 0, 10)

    # for those who have played more than 82 games, get >10 but <20mpg players
    mpg10_2010 = mpg(new_set_2010, 10, 20)
    mpg10_2000 = mpg(new_set_2000, 10, 20)

    # for those who have played more than 82 games, get >20 but <30mpg players
    mpg20_2010 = mpg(new_set_2010, 20, 30)
    mpg20_2000 = mpg(new_set_2000, 20, 30)

    # for those who have played more than 82 games, get >30 but <40mpg players
    mpg30_2010 = mpg(new_set_2010, 30, 40)
    mpg30_2000 = mpg(new_set_2000, 30, 40)

    # Is lebron in this dataset? He should be.

    # test_lebron2 = mpg30_2000[mpg30_2000['Player'] == "LeBron James"]
    # print(test_lebron2)

    print("Amount of players who have played..")
    print("")
    print("<1 season in 2000 decade:", len(one_season_2000))
    print("<1 season in 2010 decade:", len(one_season_2010))
    print("")
    print(">0 but <10 MPG in 2000 decade:", len(mpg0_2000))
    print(">0 but <10 MPG in 2010 decade:", len(mpg0_2010))
    print("")
    print(">10 but <20 MPG in 2000 decade:", len(mpg10_2000))
    print(">10 but <20 MPG in 2010 decade:", len(mpg10_2010))
    print("")
    print(">20 but <30 MPG in 2000 decade:", len(mpg20_2000))
    print(">20 but <30 MPG in 2010 decade:", len(mpg20_2010))
    print("")
    print(">30 but <40 MPG in 2000 decade:", len(mpg30_2000))
    print(">30 but <40 MPG in 2010 decade:", len(mpg30_2010))


if __name__ == '__main__':
    main()
