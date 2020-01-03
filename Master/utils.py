import pandas as pd
import numpy as np

def nearestYear(df1,df2):
    
    """
    This function takes 2 dataframe and matches the first dataframes years of the second dataframe given country
    
    For examples:
    We have the data that
    Australia GDP spend for year 1992
    The data for Australia inequality is at 1993
    
    The function returns 
    RoundedYear
    1993
    """
    # Match the year and the country with inequality dataset and than match the closest year with that countries yeardates
    # Match a year once as well
    # Get years of a given country in ineqality dataset
    new = df1
    countries = list(df1.Entity.unique())
    
    for country in countries:
        
        year_list = list(set(df2[df2.Entity == country].Year))
        for index, row in df1[df1.Entity == country].iterrows():
            # find the closest year
            year = row['Year']
            if len(year_list) > 0:
                closest = min(year_list, key=lambda x:abs(x-year))
                # Remove the matched year so it macthes only once
                year_list.remove(closest)
                new.loc[index,'RoundYear'] = closest
            else:
                new.loc[index,'RoundYear'] = None
           
    return new
