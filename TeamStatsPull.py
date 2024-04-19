import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO
import time
from sklearn.preprocessing import StandardScaler

def getTeamStats(year):
    first_year = year - 1

    base_url = 'https://fbref.com/en/comps/9/{}-{}/{}-{}-Premier-League-Stats'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_for'})
    for_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, soup, table

    for_df = for_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in for_df.columns:
        columnlist.append(index[1])

    for_df = pd.DataFrame(for_df.values, columns=columnlist)
    for_df.drop(columns=['# Pl', 'Age'], inplace=True)

    time.sleep(3)

    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_against'})
    against_df = pd.read_html(StringIO(str(table)))[0]

    del data, soup, table

    against_df = against_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in against_df.columns:
        columnlist.append(index[1])

    against_df = pd.DataFrame(against_df.values, columns=columnlist)
    against_df['Squad'] = against_df['Squad'].str[3:]
    against_df.drop(columns=['# Pl', 'Age'], inplace=True)

    prem_df = pd.merge(for_df, against_df, on='Squad', suffixes=('For', 'Against'))

    del for_df, against_df

    prem_df['Year'] = year

    prem_df.set_index(['Squad', 'Year'], inplace=True)

    scaler = StandardScaler()

    prem_df = pd.DataFrame(scaler.fit_transform(prem_df), columns=prem_df.columns, index=prem_df.index)
    prem_df.reset_index(inplace=True)

    base_url = 'https://fbref.com/en/comps/12/{}-{}/stats/{}-{}-La-Liga-Stats'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_for'})
    for_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, soup, table

    for_df = for_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in for_df.columns:
        columnlist.append(index[1])

    for_df = pd.DataFrame(for_df.values, columns=columnlist)
    for_df.drop(columns=['# Pl', 'Age'], inplace=True)

    time.sleep(3)

    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_against'})
    against_df = pd.read_html(StringIO(str(table)))[0]

    del data, soup, table

    against_df = against_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in against_df.columns:
        columnlist.append(index[1])

    against_df = pd.DataFrame(against_df.values, columns=columnlist)
    against_df['Squad'] = against_df['Squad'].str[3:]
    against_df.drop(columns=['# Pl', 'Age'], inplace=True)

    liga_df = pd.merge(for_df, against_df, on='Squad', suffixes=('For', 'Against'))

    del for_df, against_df

    liga_df['Year'] = year

    liga_df.set_index(['Squad', 'Year'], inplace=True)

    scaler = StandardScaler()

    liga_df = pd.DataFrame(scaler.fit_transform(liga_df), columns=liga_df.columns, index=liga_df.index)
    liga_df.reset_index(inplace=True)

    base_url = 'https://fbref.com/en/comps/11/{}-{}/stats/{}-{}-Serie-A-Stats'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_for'})
    for_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, soup, table

    for_df = for_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in for_df.columns:
        columnlist.append(index[1])

    for_df = pd.DataFrame(for_df.values, columns=columnlist)
    for_df.drop(columns=['# Pl', 'Age'], inplace=True)

    time.sleep(3)

    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_against'})
    against_df = pd.read_html(StringIO(str(table)))[0]

    del data, soup, table

    against_df = against_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in against_df.columns:
        columnlist.append(index[1])

    against_df = pd.DataFrame(against_df.values, columns=columnlist)
    against_df['Squad'] = against_df['Squad'].str[3:]
    against_df.drop(columns=['# Pl', 'Age'], inplace=True)

    serie_df = pd.merge(for_df, against_df, on='Squad', suffixes=('For', 'Against'))

    del for_df, against_df

    serie_df['Year'] = year

    serie_df.set_index(['Squad', 'Year'], inplace=True)

    scaler = StandardScaler()

    serie_df = pd.DataFrame(scaler.fit_transform(serie_df), columns=serie_df.columns, index=serie_df.index)
    serie_df.reset_index(inplace=True)

    base_url = 'https://fbref.com/en/comps/20/{}-{}/stats/{}-{}-Bundesliga-Stats'
    req_url = base_url.format(first_year, year, first_year, year)
    data = requests.get(req_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_for'})
    for_df = pd.read_html(StringIO(str(table)))[0]

    del base_url, req_url, soup, table

    for_df = for_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in for_df.columns:
        columnlist.append(index[1])

    for_df = pd.DataFrame(for_df.values, columns=columnlist)
    for_df.drop(columns=['# Pl', 'Age'], inplace=True)

    time.sleep(3)

    soup = BeautifulSoup(data.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'stats_squads_standard_against'})
    against_df = pd.read_html(StringIO(str(table)))[0]

    del data, soup, table

    against_df = against_df.sort_index(axis=1).drop(columns=['Playing Time', 'Performance', 'Expected'])

    columnlist = list()

    for index in against_df.columns:
        columnlist.append(index[1])

    against_df = pd.DataFrame(against_df.values, columns=columnlist)
    against_df['Squad'] = against_df['Squad'].str[3:]
    against_df.drop(columns=['# Pl', 'Age'], inplace=True)

    bund_df = pd.merge(for_df, against_df, on='Squad', suffixes=('For', 'Against'))

    del for_df, against_df

    bund_df['Year'] = year

    bund_df.set_index(['Squad', 'Year'], inplace=True)

    scaler = StandardScaler()

    bund_df = pd.DataFrame(scaler.fit_transform(bund_df), columns=bund_df.columns, index=bund_df.index)
    bund_df.reset_index(inplace=True)

    df = pd.concat([prem_df, liga_df, serie_df, bund_df], axis=0)

    del prem_df, liga_df, serie_df, bund_df

    return df