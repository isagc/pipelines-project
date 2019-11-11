import pandas as pd

from cleanDataset import getDataset
from cleanDataset import cleanDF
from webscraping import scrapeo

file_name = '../INPUT/master.csv'
df = getDataset(file_name)

drop_columns = ['country-year', 'HDI for year', 'generation']
chooseCountries = ['Denmark','Finland','Sweden','Norway', 'Iceland', 'Spain']
clean_database = cleanDF(df, drop_columns, chooseCountries)
clean_database = clean_database.reset_index()


url = 'https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration'
drop_cols = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Ref.']
paisesAelegir = ['Denmark','Finland','Sweden','Norway', 'Iceland', 'Spain']
capitales = ['Copenhagen', 'Helsinki', 'Reykjavik', 'Oslo', 'Madrid', 'Stockholm']
clean_wikipedia = scrapeo(url,drop_cols, paisesAelegir, capitales)


df_limpio = clean_database.merge(clean_wikipedia, on='Country')
df_limpio = df_limpio.set_index(['Country','Year'])
print(df_limpio)
df_limpio.to_csv('../OUTPUT/df_limpio.csv')

print(pd.read_csv('../OUTPUT/df_limpio.csv'))


