import pandas as pd 

def give_json(countries):
    # Getting url to import data
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    df = pd.read_csv(url)
    # Constraints of group C
    mask = (df['location'] == countries[0]) | (df['location'] == countries[1]) | (df['location'] == countries[2]) | (df['location'] == countries[3]) | (df['location'] == countries[4])
    # Changing date series to datetime fromat
    df['date'] = pd.to_datetime(df['date'])
    a = df[mask].groupby('date').mean()[['total_cases']]
    a = a.rename(columns={"total_cases": "t_c_averages"})
    return a.to_json()