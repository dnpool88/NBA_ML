""""
Thomas Wilson
Section AE
Final Project
Calling the dataframes, wrangling them,
combining dataframes into two big seperate decade dataframes
"""

import pandas as pd


def add_year(data, year):
    """
    add year column to dataframe to make wrangling easier
    takes in data; takes in year to assign the column to.
    this is used so we can later join these dataframes together without losing
    the information of what year we had
    """
    data["year"] = year


def read_and_edit():
    """
    reads in csv files,
    uses add_year to edit the files
    then returns 2 dataframes from merged files
    """
    # call data 2000 - 2009
    df2000 = pd.read_csv("draft/2000draft.csv")
    df2001 = pd.read_csv("draft/2001draft.csv")
    df2002 = pd.read_csv("draft/2002draft.csv")
    df2003 = pd.read_csv("draft/2003draft.csv")
    df2004 = pd.read_csv("draft/2004draft.csv")
    df2005 = pd.read_csv("draft/2005draft.csv")
    df2006 = pd.read_csv("draft/2006draft.csv")
    df2007 = pd.read_csv("draft/2007draft.csv")
    df2008 = pd.read_csv("draft/2008draft.csv")
    df2009 = pd.read_csv("draft/2009draft.csv")

    # add years to dataframe
    add_year(df2000, 2000)
    add_year(df2001, 2001)
    add_year(df2002, 2002)
    add_year(df2003, 2003)
    add_year(df2004, 2004)
    add_year(df2005, 2005)
    add_year(df2006, 2006)
    add_year(df2007, 2007)
    add_year(df2008, 2008)
    add_year(df2009, 2009)

    # call data 2010-2020
    df2010 = pd.read_csv("draft/2010draft.csv")
    df2011 = pd.read_csv("draft/2011draft.csv")
    df2012 = pd.read_csv("draft/2012draft.csv")
    df2013 = pd.read_csv("draft/2013draft.csv")
    df2014 = pd.read_csv("draft/2014draft.csv")
    df2015 = pd.read_csv("draft/2015draft.csv")
    df2016 = pd.read_csv("draft/2016draft.csv")
    df2017 = pd.read_csv("draft/2017draft.csv")
    df2018 = pd.read_csv("draft/2018draft.csv")
    df2019 = pd.read_csv("draft/2019draft.csv")
    df2020 = pd.read_csv("draft/2020draft.csv")

    # add years to dataframe
    add_year(df2010, 2010)
    add_year(df2011, 2011)
    add_year(df2012, 2012)
    add_year(df2013, 2013)
    add_year(df2014, 2014)
    add_year(df2015, 2015)
    add_year(df2016, 2016)
    add_year(df2017, 2017)
    add_year(df2018, 2018)
    add_year(df2019, 2019)
    add_year(df2020, 2020)

    df2010 = pd.concat([df2010, df2011, df2012, df2013, df2014,
                       df2015, df2016, df2017, df2018, df2019])
    df2000 = pd.concat([df2000, df2001, df2002, df2003, df2004,
                       df2005, df2006, df2007, df2008, df2009])

    return(df2010, df2000)


def main():
    pass


if __name__ == '__main__':
    main()
