#use pip install libname in the command line to install the necessary libraries below

import random
import requests
from bs4 import BeautifulSoup

#IMDb top movies URL

url="http://www.imdb.com/chart/top"

def get_year(movie_tag):
    moviesplit=movie_tag.text.split()
    year=moviesplit[-1]
    return year
   
response = requests.get(url)
html=response.text

soup=BeautifulSoup(html,'html.parser')
moviestags=soup.select('td.titleColumn')
inner_moviestags=soup.select('td.titleColumn a')
inner_moviestag=inner_moviestags[0]
rate_tags=soup.select('td.posterColumn span[name=ir]')