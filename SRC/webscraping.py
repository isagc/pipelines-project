import requests
from bs4 import BeautifulSoup
import pandas as pd



def getWikiPage(x):
    res = requests.get(x)
    html = res.text
    html[:20]
    soup = BeautifulSoup(html, 'html.parser')
    return soup
#getWikiPage(url)

def tableEurope(t):
    soup_eu = t.find_all('td')
    try :
        return {
            "Country":soup_eu[0].text.strip(),
            "City":soup_eu[1].text.strip(),
            "Jan":soup_eu[2].text.strip(),
            "Feb":soup_eu[3].text.strip(),
            "Mar":soup_eu[4].text.strip(),
            "Apr":soup_eu[5].text.strip(),
            "May":soup_eu[6].text.strip(),
            "Jun":soup_eu[7].text.strip(),
            "Jul":soup_eu[8].text.strip(),
            "Aug":soup_eu[9].text.strip(),
            "Sep":soup_eu[10].text.strip(),
            "Oct":soup_eu[11].text.strip(),
            "Nov":soup_eu[12].text.strip(),
            "Dec":soup_eu[13].text.strip(),
            "Year":soup_eu[14].text.strip(),
            "Ref.":soup_eu[15].text.strip()
        }
    except:
        return None


def scrapeo(url, drop_cols, paisesAelegir, capitales):
    # Pilla toda la pagina de wikipedia
    soup = getWikiPage(url)
    # Me quedo con la tabla del continente: "Europe"
    table_eu = soup.select('tbody')[-4].find_all('tr')
    # Creo un dataframe:
    data = pd.DataFrame(list(filter( lambda x: x ,map(lambda t: tableEurope(t), table_eu))))   
    data = data.drop(drop_cols, axis=1)   
    data = data[(data['Country'].isin(paisesAelegir))]
    data = data[(data['City'].isin(capitales))]
    data = data.rename(columns = {'Year': 'Sunshine avg hours'})
    return data
