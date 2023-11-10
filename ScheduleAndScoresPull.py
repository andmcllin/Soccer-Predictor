import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

def win(goaldiff):
    if goaldiff >= 1:
        return 2
    elif goaldiff == 0:
        return 1
    else:
        return 0

def getPastScheduleAndScores(year):
    first_year = year - 1

    base_url = 'https://fbref.com/en/comps/9/{}-{}/schedule/{}-{}-Premier-League-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_9_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    try:
        prem_scores_df = pd.read_html(StringIO(str(table)))[0]
    except:
        pass

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    prem_scores_df = prem_scores_df[['Date', 'Home', 'Score', 'Away']]
    prem_scores_df[['Home Goals', 'Away Goals']] = prem_scores_df['Score'].str.split('–', expand=True)
    prem_scores_df.dropna(inplace=True)
    prem_scores_df['Result'] = (prem_scores_df['Home Goals'].astype(int) - prem_scores_df['Away Goals'].astype(int)).apply(win)
    prem_scores_df = prem_scores_df[['Date', 'Home', 'Away', 'Result']]

    base_url = 'https://fbref.com/en/comps/12/{}-{}/schedule/{}-{}-La-Liga-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_12_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    try:
        liga_scores_df = pd.read_html(StringIO(str(table)))[0]
    except:
        pass

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    liga_scores_df = liga_scores_df[['Date', 'Home', 'Score', 'Away']]
    liga_scores_df[['Home Goals', 'Away Goals']] = liga_scores_df['Score'].str.split('–', expand=True)
    liga_scores_df.dropna(inplace=True)
    liga_scores_df['Result'] = (liga_scores_df['Home Goals'].astype(int) - liga_scores_df['Away Goals'].astype(int)).apply(win)
    liga_scores_df = liga_scores_df[['Date', 'Home', 'Away', 'Result']]

    base_url = 'https://fbref.com/en/comps/11/{}-{}/schedule/{}-{}-Serie-A-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_11_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    try:
        serie_scores_df = pd.read_html(StringIO(str(table)))[0]
    except:
        pass

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    serie_scores_df = serie_scores_df[['Date', 'Home', 'Score', 'Away']]
    serie_scores_df[['Home Goals', 'Away Goals']] = serie_scores_df['Score'].str.split('–', expand=True)
    serie_scores_df.dropna(inplace=True)
    serie_scores_df['Result'] = (serie_scores_df['Home Goals'].astype(int) - serie_scores_df['Away Goals'].astype(int)).apply(win)
    serie_scores_df = serie_scores_df[['Date', 'Home', 'Away', 'Result']]

    base_url = 'https://fbref.com/en/comps/20/{}-{}/schedule/{}-{}-Bundesliga-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_20_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    try:
        bund_scores_df = pd.read_html(StringIO(str(table)))[0]
    except:
        pass

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    bund_scores_df = bund_scores_df[['Date', 'Home', 'Score', 'Away']]
    bund_scores_df[['Home Goals', 'Away Goals']] = bund_scores_df['Score'].str.split('–', expand=True)
    bund_scores_df.dropna(inplace=True)
    bund_scores_df['Result'] = (bund_scores_df['Home Goals'].astype(int) - bund_scores_df['Away Goals'].astype(int)).apply(win)
    bund_scores_df = bund_scores_df[['Date', 'Home', 'Away', 'Result']]


    scores_df = pd.concat([prem_scores_df, liga_scores_df, serie_scores_df, bund_scores_df], axis=0)

    del prem_scores_df, liga_scores_df, serie_scores_df, bund_scores_df

    return scores_df

def getTodaysSchedule(date):   
    yearstring = date.strftime("%Y")
    today = date.strftime("%Y-%m-%d")

    if int(date.strftime("%m")) >= 7:
        year = int(yearstring) + 1
    else:
        year = int(yearstring)

    first_year = year - 1

    base_url = 'https://fbref.com/en/comps/9/{}-{}/schedule/{}-{}-Premier-League-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_9_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    prem_scores_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    prem_scores_df = prem_scores_df[['Date', 'Home', 'Away']]
    prem_scores_df.dropna(inplace=True)

    base_url = 'https://fbref.com/en/comps/12/{}-{}/schedule/{}-{}-La-Liga-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_12_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    liga_scores_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    liga_scores_df = liga_scores_df[['Date', 'Home', 'Away']]
    liga_scores_df.dropna(inplace=True)

    base_url = 'https://fbref.com/en/comps/11/{}-{}/schedule/{}-{}-Serie-A-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_11_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    serie_scores_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    serie_scores_df = serie_scores_df[['Date', 'Home', 'Away']]
    serie_scores_df.dropna(inplace=True)

    base_url = 'https://fbref.com/en/comps/20/{}-{}/schedule/{}-{}-Bundesliga-Scores-and-Fixtures'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tablestring = 'sched_{}-{}_20_1'
    modtablestring = tablestring.format(first_year, year)
    table = soup.find('table', attrs={'id': modtablestring})
    bund_scores_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, data, soup, tablestring, modtablestring, table

    bund_scores_df = bund_scores_df[['Date', 'Home', 'Away']]
    bund_scores_df.dropna(inplace=True)

    scores_df = pd.concat([prem_scores_df, liga_scores_df, serie_scores_df, bund_scores_df], axis=0)

    del prem_scores_df, liga_scores_df, serie_scores_df, bund_scores_df

    scores_df = scores_df.loc[scores_df['Date'] == today]

    return scores_df