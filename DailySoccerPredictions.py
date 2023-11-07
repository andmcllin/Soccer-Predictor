from ScheduleAndScoresPull import getTodaysSchedule
from TeamStatsPull import getTeamStats
import numpy as np
import pandas as pd
from keras.models import load_model

def makePredictions(date):
    schedule_df = getTodaysSchedule(date)

    schedule_df.rename(columns={'Home' : 'Home Team', 'Away' : 'Away Team'}, inplace=True)

    if int(date.strftime("%m")) >= 7:
        year = int(date.strftime("%Y")) + 1
    else:
        year = int(date.strftime("%Y")) 

    stats_df = getTeamStats(year)

    statscolumns = stats_df.select_dtypes(include=[np.number]).drop(columns='Year').columns

    df = pd.merge(schedule_df, stats_df, left_on='Home Team', right_on='Squad')
    df = pd.merge(df, stats_df, left_on='Away Team', right_on='Squad', suffixes=('Home', 'Away'))

    del year, schedule_df, stats_df

    for col in statscolumns:
            df[col + 'Diff'] = df[col + 'Home'] - df[col + 'Away']

    df = df[df.columns.drop(list(df.filter(regex='Home$')))]
    df = df[df.columns.drop(list(df.filter(regex='Away$')))]
    df.set_index(['Date', 'Away Team', 'Home Team'], inplace=True)
    
    model = load_model('SoccerPredictor.keras')

    try:
        predictions = pd.DataFrame(data=model.predict(df), columns=['Away Win', 'Draw', 'Home Win'])
    except:
        raise Exception('No Games Today.')

    del model

    df.reset_index(inplace=True)
    df = df[['Home Team', 'Away Team']]

    df = pd.concat([df, predictions], axis=1)

    del predictions

    for index in range(len(df)):
        winProb = df.loc[index, 'Home Win']
        winProb = round((winProb * 100), 2)
        drawProb = df.loc[index, 'Draw']
        drawProb = round((drawProb * 100), 2)
        roadProb = df.loc[index, 'Away Win']
        roadProb = round((roadProb * 100), 2)
        homeTeam = df.loc[index, 'Home Team']
        awayTeam = df.loc[index, 'Away Team']

        if winProb >= 50:
            moneyline = (int(np.round(-((100 * winProb) / (winProb - 100)), 0)))
            moneyline = "-" + str(moneyline)
        else:
            moneyline = (int(np.round(-((100 * (winProb - 100)) / (winProb)), 0)))
            moneyline = "+" + str(moneyline)

        if drawProb >= 50:
            drawmoneyline = (int(np.round(-((100 * drawProb) / (drawProb - 100)), 0)))
            drawmoneyline = "-" + str(drawmoneyline)
        else:
            drawmoneyline = (int(np.round(-((100 * (drawProb - 100)) / (drawProb)), 0)))
            drawmoneyline = "+" + str(drawmoneyline)

        if roadProb >= 50:
            roadmoneyline = (int(np.round(-((100 * roadProb) / (roadProb - 100)), 0)))
            roadmoneyline = "-" + str(roadmoneyline)
        else:
            roadmoneyline = (int(np.round(-((100 * (roadProb - 100)) / (roadProb)), 0)))
            roadmoneyline = "+" + str(roadmoneyline)

        print('Home Win for {}: {}% or {}, Draw: {}% or {}, Away Win for {}: {}% or {}'.format(homeTeam, winProb, moneyline, drawProb, drawmoneyline, awayTeam, roadProb, roadmoneyline))

    del df, winProb, drawProb, roadProb, homeTeam, awayTeam, moneyline, drawmoneyline, roadmoneyline