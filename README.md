# Covid-19-Analysis
Data Source: data.go.kr (open API)

## Objective:
* To derive and connect processed data to **Tableau** for EDA
* To visualise Covid-19 spread from Wuhan to other countries via ```markline()``` & ```markpoint()``` Tableau Functions
* To create Covid-19 Map as an interactive dashboard for a simple general trend


[Link - Covid 19 Map](https://public.tableau.com/profile/kyusang#!/vizhome/Covid-19Map_16100159410090/Dashboard1)

<img width="502" alt="covid_19_map" src="https://user-images.githubusercontent.com/35690424/103896863-9596d380-512d-11eb-9ccd-04d5dede101a.PNG">

For more detailed visuals about Covid-19, you can look through [Covid-19 Korea](https://public.tableau.com/profile/kyusang#!/vizhome/Covid-19TrendofSouthKorea/Covid-19TrendKorea)



## library used: 
_To read XML data from API_
* requests
* BeautifulSoup

_To convert XML to DataFrame and do DF work_
* pandas
* numpy

_To get latitude & longitude of Countries_
* geopy
> Simply importing 'geocode' module will cause **ImportError: No Module named...**
>> I solved this issue by import geopy on Jupyter Notebook internally
>>> ```!pip install geopy```



