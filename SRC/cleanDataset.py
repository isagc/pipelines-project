import pandas as pd


def dropColumns(df, x):
    return df.drop(x, axis = 1)



def nordicCountries(df, x):
    return df[(df['country'].isin(x))]
#df = nordicCountries(df, chooseCountries)

file_name = './INPUT/master.csv'
def getDataset(x):
    return pd.read_csv(x, encoding = "cp1252")


def genderCount(df):
    dummies = pd.get_dummies(df['sex'])
    df = pd.concat([df, dummies], axis=1)
    df['male'] = df['male']*df['suicides_no']
    df['female'] = df['female']*df['suicides_no']
    return df

def cleanDF(df, drop_columns, chooseCountries):
    df = dropColumns(df, drop_columns)
    df = nordicCountries(df, chooseCountries)
    df = genderCount(df)
    # Limpio el dataframe:
    df = df.drop(['sex'], axis=1)
    df = df.rename(columns = {'country': 'Country', 'year': 'Year', 'age': 'Age', 'suicides_no': 'total_suicides','female': 'female_suicides', 'male': 'male_suicides'})
    df = df[['Country', 'Year', 'Age', 'male_suicides', 'female_suicides', 'total_suicides', 'population','suicides/100k pop', ' gdp_for_year ($) ', 'gdp_per_capita ($)']]
    # Convierto esta columna a integro para despues poder hacerle la media:
    df[' gdp_for_year ($) '] = df[' gdp_for_year ($) '].apply(lambda x: x.replace(",", ""))
    df[' gdp_for_year ($) '] = df[' gdp_for_year ($) '].astype(int)
    # Hago la media de todas las columnas agrupando por año y país:
    df = round(df.groupby(['Country','Year']).mean(), 2)
    return df

