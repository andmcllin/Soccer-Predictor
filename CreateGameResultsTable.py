from ScheduleAndScoresPull import getPastScheduleAndScores
from TeamStatsPull import getTeamStats
import pandas as pd
import numpy as np

def createGameResultsCSV(startyear, endyear):
    years = np.arange(startyear, endyear, 1)

    df = pd.DataFrame()

    for year in years:
        scores_df = getPastScheduleAndScores(year)

        teamstats_df = getTeamStats(year)

        scores_df.rename(columns={'Home' : 'Home Team', 'Away' : 'Away Team'}, inplace=True) 
        statscolumns = teamstats_df.select_dtypes(include=[np.number]).drop(columns='Year').columns

        merged_df = pd.merge(scores_df, teamstats_df, left_on='Home Team', right_on='Squad')
        merged_df = pd.merge(merged_df, teamstats_df, left_on='Away Team', right_on='Squad', suffixes=('Home', 'Away'))

        del scores_df, teamstats_df

        for col in statscolumns:
            merged_df[col + 'Diff'] = merged_df[col + 'Home'] - merged_df[col + 'Away']

        merged_df = merged_df[merged_df.columns.drop(list(merged_df.filter(regex='Home$')))]
        merged_df = merged_df[merged_df.columns.drop(list(merged_df.filter(regex='Away$')))]

        df = pd.concat([df, merged_df])

    del merged_df

    df.to_csv('soccerGameResults.csv.gz', compression={'method':'gzip'}, index=False)