def give_json(country1, country2, country3, country4, country5):
    # Importing library
    import pandas as pd
    # Getting url to import data
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    df = pd.read_csv(url)
    # Constraints of group C
    mask = (df['location'] == country1) | (df['location'] == country2) | (df['location'] == country3) | (df['location'] == country4) | (df['location'] == country5)
    # Changing date series to datetime fromat
    df['date'] = pd.to_datetime(df['date'])
    a = df[mask].groupby('date').mean()[['total_cases']]
    a = a.rename(columns={"total_cases": "t_c_avg"})
    return a.to_json()