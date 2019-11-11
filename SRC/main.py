
import argparse
import subprocess
import pandas as pd

def parametros():
    parser = argparse.ArgumentParser(description='This pipeline links number of suicides, in given country and year, to sunshine average hours in said country.')
    parser.add_argument('-c', '--country', help='Choose from any of the nordic countries or Spain', type=str)
    parser.add_argument('-y', '--year', help='Choose any year between 1984 and 2016. In case there is no data available for given year, the program will ask you to try with a different one.', type=int)
    args = parser.parse_args()
    return args

def main():
    config = parametros()
    df = pd.read_csv('../OUTPUT/df_limpio.csv')

    def find_info(df,c,y):
        df_search = df[df['Country']==c]
        df_2 = df_search[df_search['Year']==y]
        return df_2

    try:
        results = find_info(df,config.country,config.year)
        r1 = results['male_suicides'].values
        r2 = results['female_suicides'].values
        r3 = results['total_suicides'].values
        r4 = results['Sunshine avg hours'].values    
        return ("On average, there were {} total suicides. {} of them were accounted to men and {} were accounted to women. Moreover, there was an average sunshine duration of {} hours".format(r3[0], r1[0], r2[0], r4[0]))
    except:
       return "There is no data available for this year. Please choose another year"

if __name__=='__main__':
	print(main())
