def give_json(df, countries, column_of_interest):
    """
    This function receives a pandas dataframe, a list of countries of interest
    and a string with the name of the column of interest. It groups the countries 
    by date and calculates the average value of the column of interest.
    After the data is grouped the function returns it in json format.
    """
    mask = df['location'].isin(countries)
    a = df[mask].groupby('date').mean()[[column_of_interest]]
    a = a.rename(columns={"total_cases": "t_c_averages"})
    return a.to_json()


def filter_countries(df, countries):
    """
    This function receives a pandas dataframe and a list of countries of interest.
    It returns a filtered dataframe that only contains
    the rows of the countries of interest
    """
    mask = df['location'].isin(countries)
    return df[mask]