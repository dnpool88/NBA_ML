"""
Samir Ouijdani
Section AE
Final Project

This file takes in a csv file, turns it into multiple
dataframes and visualizes them so we can answer the question
how have NBA Conferences, Divisons, and Teams performed against
each other over the past two decades?"
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


def plot_team_graph(team, df2):
    """
    This function takes in a 3 letter string abbreviation for a team (EX:
    SAS for San Antonio Spurs) and will save an image of that team's
    win coefficient per season since 2004-2005. It will be named
    team abbreviation Over Time
    """
    g = sns.catplot(x="Season", y=team, kind='bar', data=df2)
    g.refline(y=1)
    plt.xticks(rotation=45)
    plt.title(team + ' Win Coefficeint Over Time')
    plt.savefig(team + ' Over Time')


def conferences_plot(east_plot, west_plot):
    """
    This plot takes in the eastern and western teams in the form of a dataframe
    and saves an image of a plot that displays the nba conferences since
    2003-2004 the lines are a direct reflection of each other as the
    mean win coefficients of each season should add to two
    """
    data = [east_plot["east_mean_win_coef"], west_plot["west_mean_win_coef"],
            west_plot["Season"]]
    headers = ["East", "West", "Season"]
    df3 = pd.concat(data, axis=1, keys=headers)
    df4 = df3.melt('Season', var_name='Conference',
                   value_name='Win Coefficeint')
    sns.catplot(x="Season", y="Win Coefficeint", hue='Conference',
                data=df4, kind='point')
    plt.xticks(rotation=45)
    plt.title('NBA Conferences Since 2003-2004')
    plt.savefig('Conferences over Time')


def divisional_plot(Atlantic_Division, Central_Division,
                    Southeast_Division, Pacific_Division,
                    Northwest_Division, Southwest_Division):
    """
    This function takes in 6 dataframes, one for each division in the NBA,
    in return this plot produces a figure containing 6 graphs,
    one for each division, displaying the win
    coefficients by season over time.
    """
    Atlantic_Plot = Atlantic_Division.melt('Season', var_name='Team',
                                           value_name='Win Coefficeint')
    Central_Plot = Central_Division.melt('Season', var_name='Team',
                                         value_name='Win Coefficeint')
    Southeast_Plot = Southeast_Division.melt('Season', var_name='Team',
                                             value_name='Win Coefficeint')
    Pacific_Plot = Pacific_Division.melt('Season', var_name='Team',
                                         value_name='Win Coefficeint')
    Northwest_Plot = Northwest_Division.melt('Season', var_name='Team',
                                             value_name='Win Coefficeint')
    Southwest_Plot = Southwest_Division.melt('Season', var_name='Team',
                                             value_name='Win Coefficeint')

    fig, [[ax1, ax2], [ax3, ax4], [ax5, ax6]] = plt.subplots(3, 2,
                                                             figsize=(30, 18))
    sns.barplot(x="Season", y="Win Coefficeint", hue='Team',
                data=Atlantic_Plot, ax=ax1)
    ax1.set_title('Eastern Confernce: Atlantic Division')
    sns.barplot(x="Season", y="Win Coefficeint", hue='Team',
                data=Central_Plot, ax=ax5)
    ax5.set_title('Eastern Confernce: Central Division')
    sns.barplot(x="Season", y="Win Coefficeint", hue='Team',
                data=Southeast_Plot, ax=ax3)
    ax3.set_title('Eastern Confernce: Southeast Division')
    sns.barplot(x="Season", y="Win Coefficeint", hue='Team',
                data=Pacific_Plot, ax=ax4)
    ax4.set_title('Western Confernce: Pacific Division')
    sns.barplot(x="Season", y="Win Coefficeint", hue='Team',
                data=Northwest_Plot, ax=ax2)
    ax2.set_title('Western Confernce: Northwest Division')
    sns.barplot(x="Season", y="Win Coefficeint", hue='Team',
                data=Southwest_Plot, ax=ax6)
    ax6.set_title('Western Confernce: Southwest Division')
    fig.suptitle('NBA DIVISIONS IN 3 ERAS', fontsize=30)
    for i in ax1.containers:
        ax1.bar_label(i, label_type='center')
    for i in ax2.containers:
        ax2.bar_label(i, label_type='center')
    for i in ax3.containers:
        ax3.bar_label(i, label_type='center')
    for i in ax4.containers:
        ax4.bar_label(i, label_type='center')
    for i in ax5.containers:
        ax5.bar_label(i, label_type='center')
    for i in ax6.containers:
        ax6.bar_label(i, label_type='center')
    plt.savefig('divisions.png', bbox_inches='tight')


def main():
    df = pd.read_csv('wins_since_2000.csv')
    df = df.iloc[0:18:1, :]
    df['Sum'] = df.loc[:, "ATL":"WAS":1].sum(axis=1)
    df['mean_wins'] = df['Sum'] / (30)
    df2 = df.loc[:, "ATL":"mean_wins": 1].div(df.mean_wins, axis=0)
    season = df['Season']
    df2['Season'] = season
    east_conf_coef = df2.loc[:, ['ATL', 'BOS', 'BRK', 'CHI',
                                 'CHO', 'CLE', 'DET', 'IND',
                                 'MIA', 'MIL', 'NYK', 'ORL',
                                 'PHI', 'TOR', 'WAS', 'Season']]
    west_conf_coef = df2.loc[:, ['DAL', 'DEN', 'GSW', 'HOU',
                                 'LAC', 'LAL', 'MEM', 'MIN',
                                 'NOP', 'OKC', 'PHO', 'POR',
                                 'SAC', 'SAS', 'UTA', 'Season']]
    df_divisional = df2.iloc[0:18:8, :]
    df_divisional = df_divisional.round(3)
    Atlantic_Division = df_divisional.loc[:, ['PHI', 'BOS', 'TOR',
                                              'NYK', 'BRK', 'Season']]
    Central_Division = df_divisional.loc[:, ['MIL', 'CHI', 'CLE',
                                             'IND', 'DET', 'Season']]
    Southeast_Division = df_divisional.loc[:, ['MIA', 'ATL', 'CHO',
                                               'WAS', 'ORL', 'Season']]
    Northwest_Division = df_divisional.loc[:, ['UTA', 'DEN', 'MIN',
                                               'POR', 'OKC', 'Season']]
    Pacific_Division = df_divisional.loc[:, ['PHO', 'GSW', 'LAC',
                                             'LAL', 'SAC', 'Season']]
    Southwest_Division = df_divisional.loc[:, ['MEM', 'DAL', 'NOP',
                                               'SAS', 'HOU', 'Season']]
    west_conf_coef['Sum'] = west_conf_coef.loc[:, "DAL":"UTA":1].sum(axis=1)
    west_conf_coef['west_mean_win_coef'] = west_conf_coef['Sum'] / (15)
    east_conf_coef['Sum'] = east_conf_coef.loc[:, "ATL":"WAS":1].sum(axis=1)
    east_conf_coef['east_mean_win_coef'] = east_conf_coef['Sum'] / (15)
    east_plot = east_conf_coef.iloc[0:18:2, :]
    west_plot = west_conf_coef.iloc[0:18:2, :]

    conferences_plot(east_plot, west_plot)
    divisional_plot(Atlantic_Division, Central_Division, Southeast_Division,
                    Pacific_Division, Northwest_Division, Southwest_Division)
    plot_team_graph('MIL', df2)


if __name__ == '__main__':
    main()
