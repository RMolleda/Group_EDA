def give_json(df, countries, column_of_interest):
    mask = df['location'].isin(countries)
    a = df[mask].groupby('date').mean()[[column_of_interest]]
    a = a.rename(columns={"total_cases": "t_c_averages"})
    return a.to_json()