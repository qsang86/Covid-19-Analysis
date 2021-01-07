import pandas as pd
import requests
from bs4 import BeautifulSoup


def open_api_reader():
    open_api_key = 'VwUNnuPS5treeoYbtM8R2Cw89HPvmvApECDi28RBhaY4z2eFUCx2WjEXUm1w%2B6iibQjSA5FxoeCMm3Pj5YDlhA%3D%3D'
    params = '&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200315'

    #url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?ServiceKey=' + open_api_key + params
    #end_point = 'http://openapi.data.go.kr/openapi/service/rest/Covid19'
    open_url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson?serviceKey=VwUNnuPS5treeoYbtM8R2Cw89HPvmvApECDi28RBhaY4z2eFUCx2WjEXUm1w%2B6iibQjSA5FxoeCMm3Pj5YDlhA%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200414'


    res = requests.get(open_url).text.encode('utf-8')
    soup = BeautifulSoup(res, 'lxml-xml')

    rows = soup.findAll('item')
    columns = rows[0].find_all()

    rowlist = []
    collist = []
    tlist = []

    for i in range(0, len(rows)):
        columns = rows[i].find_all()
        for j in range(0, len(columns)):
            if i == 0:
                tlist.append(columns[j].name)
            col_ = columns[j].text
            collist.append(col_)
        rowlist.append(collist)
        collist = []

    result_df = pd.DataFrame(rowlist, columns=tlist)
    print('number of rows: ', len(result_df.index))

    return result_df


!pip install geopy
import numpy as np

def get_geocode(city): 
    try: 
        geoloc = Nominatim(user_agent="covid19") 
        
        ##timeout = set unlimited time to run.
        ##too much time taken -> going to improve
        return geoloc.geocode(city, timeout=None) 
    except GeocoderTimedOut: 
        return get_geocode(city)    


def add_lat_long(df):
	longitude = []
	latitude = []

	for i in (df):
	    if get_geocode(i) != None:
	        location = get_geocode(i)
	         
	        latitude.append(location.latitude)
	        longitude.append(location.longitude)
	    
	    else:
	        latitude.append(np.nan)
	        longitude.append(np.nan)

	df['latitude'] = latitude
	df['longitude'] = longtude
	df = df.dropna()
	return df


def main():

	df_covid = open_api_reader()
	df_covid = result_df[['areaNmEn', 'nationNmEn', 'createDt', 'natDeathCnt', 'natDeathRate', 'natDefCnt']]
	add_lat_long(df_covid)
	df_covid.to_excel('./covid_19.xlsx', index = False)


if __name__ == '__main__':
	main()


