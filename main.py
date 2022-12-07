# This is a sample Python script.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
data_sample = data.loc[:, ['Name', 'Platform', 'Genre', 'Publisher', 'Global_Sales']].head()
print(data_sample)


def create_moving_average(df):
    total = df.groupby(['Year_of_Release', 'Genre']).sum()
    moving_average = total.reset_index()
    moving_average = moving_average[moving_average['Year_of_Release'] <= 2015]
    moving_average['Moving_Average'] = moving_average['Global_Sales'].rolling(window=5).mean()
    return moving_average


def create_count(df):
    copies_per_year = df.drop(columns=['Global_Sales']).set_index('Year_of_Release').sort_index()
    copies_per_year = copies_per_year.groupby(['Year_of_Release', 'Genre']).size().reset_index()
    copies_per_year = copies_per_year.set_axis(['Year_of_Release', 'Genre', 'Frequency'], axis=1)
    return copies_per_year


def genreScatterPlot():
    data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
    # getting relevant data
    selected_data = data.loc[:, ['Name', 'Platform', 'Genre', 'Year_of_Release', 'Publisher', 'Global_Sales']].dropna()
    selected_data = selected_data[selected_data['Year_of_Release'] <= 2015]
    selected_data_2 = selected_data.groupby('Name')['Global_Sales'].sum().to_frame().reset_index().set_axis(
        ['Name', 'Global_Sales'], axis=1).set_index('Name')
    selected_data = selected_data.drop(['Global_Sales'], axis=1).drop_duplicates(subset=['Name'],
                                                                                 keep='first').set_index('Name')
    final_selected_data = selected_data.merge(selected_data_2, left_index=True, right_index=True)[
        ['Year_of_Release', 'Genre', 'Global_Sales']]

    plot_data = final_selected_data.set_index(['Year_of_Release', 'Genre']).sort_index().dropna()
    #getting data set within std
    std_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).std().fillna(0)
    low_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).mean().subtract(std_by_year_genre)
    high_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).mean().add(std_by_year_genre)
    #readying data sets to be outputted
    plot_data = plot_data.merge(low_by_year_genre, left_index=True, right_index=True).merge(high_by_year_genre, left_index=True, right_index=True)
    plot_data = plot_data.set_axis(['Global_Sales', 'Std_Low_End_Global_Sales', 'Std_High_End_Global_Sales'], axis=1)
    plot_data_2 = plot_data[(plot_data['Std_Low_End_Global_Sales'] <= plot_data['Global_Sales']) & ( plot_data['Global_Sales'] <= plot_data['Std_High_End_Global_Sales'])]
    plot_data_2 = plot_data_2.drop(plot_data.columns[[1, 2]], axis=1)
    # formating and outputting plots
    custom_style = {
        'axes.edgecolor': 'gray',
        'axes.facecolor': 'lightgray',
        'axes.labelcolor': 'black',
        'grid.color': 'black',
        'text.color': 'black',
        'xtick.color': 'black',
        'ytick.color': 'black',
    }

    sns.set_style("darkgrid", rc=custom_style)
    sns.set_context("paper")

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    fig.subplots_adjust(hspace=.3, wspace=.2)

    plt.subplot(1, 2, 1)
    p1 = sns.scatterplot(data=plot_data, x='Year_of_Release', y='Global_Sales', hue='Genre')
    p1.set(xlabel='Years', ylabel='Number of Sales(millions', title='Sales by Genre Over Time')

    plt.subplot(1, 2, 2)
    p2 = sns.scatterplot(data=plot_data_2, x='Year_of_Release', y='Global_Sales', hue='Genre')
    p2.set(xlabel='Years', ylabel='Number of Sales(millions', title='Sales by Genre Over Time(STD)')

    plt.show()


def movingAvgAndNumSoldGenre():
    data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

    # selecting for Genre Year and Sales and removing incomplete data
    selected_data = data.loc[:, ['Name', 'Platform', 'Genre', 'Year_of_Release', 'Publisher', 'Global_Sales']].dropna()
    selected_data = selected_data[selected_data['Year_of_Release'] <= 2015]
    selected_data_2 = selected_data.groupby('Name')['Global_Sales'].sum().to_frame().reset_index().set_axis(
        ['Name', 'Global_Sales'], axis=1).set_index('Name')
    selected_data = selected_data.drop(['Global_Sales'], axis=1).drop_duplicates(subset=['Name'],
                                                                                 keep='first').set_index('Name')
    final_selected_data = selected_data.merge(selected_data_2, left_index=True, right_index=True)[
        ['Year_of_Release', 'Genre', 'Global_Sales']]
    # getting std data from data
    std_by_year_genre = final_selected_data.groupby(['Year_of_Release', 'Genre']).std().fillna(0)
    std_low_by_year_genre = final_selected_data.groupby(['Year_of_Release', 'Genre']).mean().subtract(std_by_year_genre)
    std_high_by_year_genre = final_selected_data.groupby(['Year_of_Release', 'Genre']).mean().add(std_by_year_genre)

    plot_data_std = final_selected_data.set_index(['Year_of_Release', 'Genre']).sort_index()
    plot_data_std = plot_data_std.merge(std_low_by_year_genre, left_index=True, right_index=True).merge(
        std_high_by_year_genre, left_index=True, right_index=True)
    plot_data_std = plot_data_std.set_axis(['Global_Sales', 'Std_Low_End_Global_Sales', 'Std_High_End_Global_Sales'],
                                           axis=1)
    plot_data_std = plot_data_std[(plot_data_std['Std_Low_End_Global_Sales'] <= plot_data_std['Global_Sales']) & (
            plot_data_std['Global_Sales'] <= plot_data_std['Std_High_End_Global_Sales'])]
    plot_data_std = plot_data_std.drop(plot_data_std.columns[[1, 2]], axis=1).reset_index()

    # finding moving average
    moving_average_by_year_genre = create_moving_average(final_selected_data)

    # finding the total amount of titles released per year
    game_count_by_year_genre = create_count(final_selected_data)

    moving_average_by_year_genre_std = create_moving_average(plot_data_std)

    game_count_by_year_genre_std = create_count(plot_data_std)
    # formating and outputting plots
    custom_style = {
        'axes.edgecolor': 'darkgray',
        'axes.facecolor': 'darkgray',
        'axes.labelcolor': 'black',
        'grid.color': 'black',
        'text.color': 'black',
        'xtick.color': 'black',
        'ytick.color': 'black',
    }

    sns.set_style("darkgrid", rc=custom_style)
    sns.set_context("paper")

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 7))
    fig.subplots_adjust(hspace=.3, wspace=.2)

    p1 = sns.lineplot(ax=axes[0, 0], data=moving_average_by_year_genre, x='Year_of_Release', y='Moving_Average',
                      hue='Genre')
    p1.set(xlabel='Years', ylabel='5 Year Moving Average of Sales(Millions)',
           title='5 Year Moving Average Sales by Genre OverTime')

    p2 = sns.lineplot(ax=axes[0, 1], data=game_count_by_year_genre, x='Year_of_Release', y='Frequency', hue='Genre')
    p2.set(xlabel='Years', ylabel='Number of Titles', title='Number of Titles Published by Genre Over Time')

    p3 = sns.lineplot(ax=axes[1, 0], data=moving_average_by_year_genre_std, x='Year_of_Release', y='Moving_Average',
                      hue='Genre')
    p3.set(xlabel='Years', ylabel='5 Year Moving Average of Sales(Millions)',
           title='5 Year Moving Average Sales by Genre OverTime(Within STD)')

    p4 = sns.lineplot(ax=axes[1, 1], data=game_count_by_year_genre_std, x='Year_of_Release', y='Frequency', hue='Genre')
    p4.set(xlabel='Years', ylabel='Number of Titles', title='Number of Titles Published by Genre Over Time(Within STD)')

    plt.rc("savefig", dpi=300)
    plt.rcParams['figure.dpi'] = 300
    plt.show()


def genreLinePlot():
    data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
    # getting relevant data
    selected_data = data.loc[:, ['Name', 'Platform', 'Genre', 'Year_of_Release', 'Publisher', 'Global_Sales']].dropna()
    selected_data = selected_data[selected_data['Year_of_Release'] <= 2015]
    selected_data_2 = selected_data.groupby('Name')['Global_Sales'].sum().to_frame().reset_index().set_axis(
        ['Name', 'Global_Sales'], axis=1).set_index('Name')
    selected_data = selected_data.drop(['Global_Sales'], axis=1).drop_duplicates(subset=['Name'],
                                                                                 keep='first').set_index('Name')
    final_selected_data = selected_data.merge(selected_data_2, left_index=True, right_index=True)[
        ['Year_of_Release', 'Genre', 'Global_Sales']]

    plot_data = final_selected_data.set_index(['Year_of_Release', 'Genre']).sort_index().dropna()
    # getting std data from data
    std_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).std().fillna(0)
    low_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).mean().subtract(std_by_year_genre)
    high_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).mean().add(std_by_year_genre)

    plot_data = plot_data.merge(low_by_year_genre, left_index=True, right_index=True).merge(high_by_year_genre,
                                                                                            left_index=True,
                                                                                            right_index=True)
    plot_data = plot_data.set_axis(['Global_Sales', 'Std_Low_End_Global_Sales', 'Std_High_End_Global_Sales'], axis=1)

    plot_data_2 = plot_data[(plot_data['Std_Low_End_Global_Sales'] <= plot_data['Global_Sales']) & (
            plot_data['Global_Sales'] <= plot_data['Std_High_End_Global_Sales'])]
    plot_data_2 = plot_data_2.drop(plot_data.columns[[1, 2]], axis=1)
    # grouping genre with year and getting total yearly sales for each genre for both sets of data
    global_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).sum()
    global_by_year_genre_std = plot_data_2.groupby(['Year_of_Release', 'Genre']).sum()
    # formating and outputting plots
    custom_style = {
        'axes.edgecolor': 'gray',
        'axes.facecolor': 'lightgray',
        'axes.labelcolor': 'black',
        'grid.color': 'black',
        'text.color': 'black',
        'xtick.color': 'black',
        'ytick.color': 'black',
    }

    sns.set_style("darkgrid", rc=custom_style)
    sns.set_context("paper")

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    fig.subplots_adjust(hspace=.3, wspace=.2)

    plt.subplot(1, 2, 1)
    p1 = sns.lineplot(data=global_by_year_genre, x='Year_of_Release', y='Global_Sales', hue='Genre')
    p1.set(xlabel='Years', ylabel='Number of Sales(millions', title='Sales by Genre Over Time')

    plt.subplot(1, 2, 2)
    p2 = sns.lineplot(data=global_by_year_genre_std, x='Year_of_Release', y='Global_Sales', hue='Genre')
    p2.set(xlabel='Years', ylabel='Number of Sales(millions', title='Sales by Genre Over Time(STD)')

    plt.show()


def publisherLinePlot():
    data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
    # getting relevant data
    plot_data = data.loc[:, ['Year_of_Release', 'Global_Sales', 'Publisher', 'Genre']]
    # getting rid of all non action titles from data
    plot_data = plot_data[plot_data.Genre == 'Action']
    plot_data = plot_data[plot_data['Year_of_Release'] <= 2015]
    del plot_data['Genre']
    # selecting relevant publishers
    plot_data = plot_data[(plot_data.Publisher == 'Activision') | (plot_data.Publisher == 'Nintendo') | (
            plot_data.Publisher == 'Electronic Arts')
                          | (plot_data.Publisher == 'Konami Digital Entertainment') | (
                                  plot_data.Publisher == 'Sega') | (plot_data.Publisher == 'Sega') | (
                                  plot_data.Publisher == 'Sony Computer Entertainment')
                          | (plot_data.Publisher == 'THQ') | (plot_data.Publisher == 'Take-Two Interactive') | (
                                  plot_data.Publisher == 'Ubisoft') | (plot_data.Publisher == 'Namco Bandai Games')]

    plot_data = plot_data.set_index(['Year_of_Release', 'Publisher']).sort_index().dropna()

    std_by_year_genre = plot_data.groupby(['Year_of_Release', 'Publisher']).std().fillna(0)
    low_by_year_genre = plot_data.groupby(['Year_of_Release', 'Publisher']).mean().subtract(std_by_year_genre)
    high_by_year_genre = plot_data.groupby(['Year_of_Release', 'Publisher']).mean().add(std_by_year_genre)

    plot_data = plot_data.merge(low_by_year_genre, left_index=True, right_index=True).merge(high_by_year_genre,
                                                                                            left_index=True,
                                                                                            right_index=True)
    plot_data = plot_data.set_axis(['Global_Sales', 'Std_Low_End_Global_Sales', 'Std_High_End_Global_Sales'], axis=1)

    plot_data_2 = plot_data[(plot_data['Std_Low_End_Global_Sales'] <= plot_data['Global_Sales']) & (
            plot_data['Global_Sales'] <= plot_data['Std_High_End_Global_Sales'])]
    plot_data_2 = plot_data_2.drop(plot_data.columns[[1, 2]], axis=1)
    # summing total sales per year for each publisher for each data set
    global_by_year_publsher = plot_data.groupby(['Year_of_Release', 'Publisher']).sum()
    global_by_year_publsher_std = plot_data_2.groupby(['Year_of_Release', 'Publisher']).sum()
    # formating and outputting plots
    custom_style = {
        'axes.edgecolor': 'gray',
        'axes.facecolor': 'lightgray',
        'axes.labelcolor': 'black',
        'grid.color': 'black',
        'text.color': 'black',
        'xtick.color': 'black',
        'ytick.color': 'black',
    }

    sns.set_style("darkgrid", rc=custom_style)
    sns.set_context("paper")

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    fig.subplots_adjust(hspace=.3, wspace=.2)

    plt.subplot(1, 2, 1)
    p1 = sns.lineplot(data=global_by_year_publsher, x='Year_of_Release', y='Global_Sales', hue='Publisher')
    p1.set(xlabel='Years', ylabel='Number of Sales(millions', title='Action Game Sales by Publisher Over Time')

    plt.subplot(1, 2, 2)
    p2 = sns.lineplot(data=global_by_year_publsher_std, x='Year_of_Release', y='Global_Sales', hue='Publisher')
    p2.set(xlabel='Years', ylabel='Number of Sales(millions', title='Action Game Sales by Publisher Over Time(STD)')

    plt.show()


def platformLinePlot():
    data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
    # getting relevant data
    plot_data = data.loc[:, ['Year_of_Release', 'Global_Sales', 'Platform', 'Genre']]
    # getting rid of all non action titles from data
    plot_data = plot_data[plot_data.Genre == 'Action']
    plot_data = plot_data[plot_data['Year_of_Release'] <= 2015]
    del plot_data['Genre']
    # getting relevant platforms
    plot_data = plot_data[(plot_data.Platform == '3DS') | (plot_data.Platform == 'DS') | (
            plot_data.Platform == 'GBA')
                          | (plot_data.Platform == 'PS') | (
                                  plot_data.Platform == 'PS2') | (plot_data.Platform == 'PS3') | (
                                  plot_data.Platform == 'PS4')
                          | (plot_data.Platform == 'PSP') | (plot_data.Platform == 'WII') | (
                                  plot_data.Platform == 'X360') | (plot_data.Platform == 'XB')]

    plot_data = plot_data.set_index(['Year_of_Release', 'Platform']).sort_index().dropna()
    # getting std for data set
    std_by_year_genre = plot_data.groupby(['Year_of_Release', 'Platform']).std().fillna(0)
    low_by_year_genre = plot_data.groupby(['Year_of_Release', 'Platform']).mean().subtract(std_by_year_genre)
    high_by_year_genre = plot_data.groupby(['Year_of_Release', 'Platform']).mean().add(std_by_year_genre)

    plot_data = plot_data.merge(low_by_year_genre, left_index=True, right_index=True).merge(high_by_year_genre,
                                                                                            left_index=True,
                                                                                            right_index=True)
    plot_data = plot_data.set_axis(['Global_Sales', 'Std_Low_End_Global_Sales', 'Std_High_End_Global_Sales'], axis=1)

    plot_data_2 = plot_data[(plot_data['Std_Low_End_Global_Sales'] <= plot_data['Global_Sales']) & (
            plot_data['Global_Sales'] <= plot_data['Std_High_End_Global_Sales'])]
    plot_data_2 = plot_data_2.drop(plot_data.columns[[1, 2]], axis=1)
    # getting total sales per year for each platform
    global_by_year_platform = plot_data.groupby(['Year_of_Release', 'Platform']).sum()
    global_by_year_platform_std = plot_data_2.groupby(['Year_of_Release', 'Platform']).sum()
    # formating and outputting plots
    custom_style = {
        'axes.edgecolor': 'gray',
        'axes.facecolor': 'lightgray',
        'axes.labelcolor': 'black',
        'grid.color': 'black',
        'text.color': 'black',
        'xtick.color': 'black',
        'ytick.color': 'black',
    }

    sns.set_style("darkgrid", rc=custom_style)
    sns.set_context("paper")

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    fig.subplots_adjust(hspace=.3, wspace=.2)

    plt.subplot(1, 2, 1)
    p1 = sns.lineplot(data=global_by_year_platform, x='Year_of_Release', y='Global_Sales', hue='Platform')
    p1.set(xlabel='Years', ylabel='Number of Sales(millions', title='Action Game Sales by Platform Over Time')

    plt.subplot(1, 2, 2)
    p2 = sns.lineplot(data=global_by_year_platform_std, x='Year_of_Release', y='Global_Sales', hue='Platform')
    p2.set(xlabel='Years', ylabel='Number of Sales(millions', title='Action Game Sales by Platform Over Time(STD)')

    plt.show()


def marketShareGenre():
    data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
    # getting relevant data
    selected_data = data.loc[:, ['Name', 'Platform', 'Genre', 'Year_of_Release', 'Publisher', 'Global_Sales']].dropna()
    selected_data = selected_data[selected_data['Year_of_Release'] <= 2015]
    selected_data_2 = selected_data.groupby('Name')['Global_Sales'].sum().to_frame().reset_index().set_axis(
        ['Name', 'Global_Sales'], axis=1).set_index('Name')
    selected_data = selected_data.drop(['Global_Sales'], axis=1).drop_duplicates(subset=['Name'],
                                                                                 keep='first').set_index('Name')
    final_selected_data = selected_data.merge(selected_data_2, left_index=True, right_index=True)[
        ['Year_of_Release', 'Genre', 'Global_Sales']]

    plot_data = final_selected_data.set_index(['Year_of_Release', 'Genre']).sort_index().dropna()

    # getting std of given data
    std_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).std().fillna(0)
    low_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).mean().subtract(std_by_year_genre)
    high_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).mean().add(std_by_year_genre)

    plot_data = plot_data.merge(low_by_year_genre, left_index=True, right_index=True).merge(high_by_year_genre,
                                                                                            left_index=True,
                                                                                            right_index=True)
    plot_data = plot_data.set_axis(['Global_Sales', 'Std_Low_End_Global_Sales', 'Std_High_End_Global_Sales'], axis=1)

    plot_data_2 = plot_data[(plot_data['Std_Low_End_Global_Sales'] <= plot_data['Global_Sales']) & (
            plot_data['Global_Sales'] <= plot_data['Std_High_End_Global_Sales'])]
    plot_data_2 = plot_data_2.drop(plot_data.columns[[1, 2]], axis=1)

    # calculating market share for non std data
    global_by_year_genre = plot_data.groupby(['Year_of_Release', 'Genre']).sum()
    global_by_year = plot_data.groupby(['Year_of_Release']).sum()
    market_share_by_year_genre = global_by_year_genre.divide(global_by_year, axis=0).reset_index()

    # calculating market share for std data
    global_by_year_genre_std = plot_data_2.groupby(['Year_of_Release', 'Genre']).sum()
    global_by_year_std = plot_data_2.groupby(['Year_of_Release']).sum()
    market_share_by_year_genre_std = global_by_year_genre_std.divide(global_by_year_std, axis=0).reset_index()

    # formating and outputting plots
    custom_style = {
        'axes.edgecolor': 'gray',
        'axes.facecolor': 'lightgray',
        'axes.labelcolor': 'black',
        'grid.color': 'black',
        'text.color': 'black',
        'xtick.color': 'black',
        'ytick.color': 'black',
    }

    sns.set_style("darkgrid", rc=custom_style)
    sns.set_context("paper")

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    fig.subplots_adjust(hspace=.3, wspace=.2)

    plt.subplot(1, 2, 1)
    p1 = sns.lineplot(data=market_share_by_year_genre, x='Year_of_Release', y='Global_Sales', hue='Genre')
    p1.set(xlabel='Years', ylabel='Percent', title='Market Share by Genre')

    plt.subplot(1, 2, 2)
    p2 = sns.lineplot(data=market_share_by_year_genre_std, x='Year_of_Release', y='Global_Sales', hue='Genre')
    p2.set(xlabel='Years', ylabel='Percent', title='Market Share by Genre(STD)')

    plt.show()


genreScatterPlot()
genreLinePlot()#Conley Deleon
publisherLinePlot()#Conley Deleon
movingAvgAndNumSoldGenre()
platformLinePlot()#Conley Deleon
marketShareGenre()
