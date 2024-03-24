from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.metacritic.com/movie/"
user_agent= {"User-agent":'Mozilla/5.0'}
data = requests.get(url=URL, headers=user_agent)
soup = BeautifulSoup(data.content, "html.parser")


# Storing new releases
new_releases=[]

new_releases_soup = soup.find_all("div", 
                                  class_="c-globalCarousel_content c-globalCarousel_content-scrollable c-globalCarousel_content-scrollable_gap-medium c-globalCarousel_content-scrollable_mobile-gap-small")[0]

for i in new_releases_soup:
    isim = i.h3.text
    puan = i.span.text
    movie_dict = {"film_adi":isim, "film_puani":puan}
    new_releases.append(movie_dict)
        



# Creating dataframe

film_adlari = []
film_puanlari= []

for film in new_releases:
    film_adlari.append(film["film_adi"])
    film_puanlari.append(film["film_puani"]) 

film_adlari = pd.Series(film_adlari)
film_puanlari = pd.Series(film_puanlari)

movie_series = pd.concat([film_adlari, film_puanlari], axis=1)


df = pd.DataFrame(movie_series)
df.columns = ["film_adlari", "film_puanlari"]

df.to_excel(excel_writer="metacritic_output.xlsx", header=False, index=False)