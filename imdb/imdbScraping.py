from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

page_html = BeautifulSoup(response.text, "html.parser")

table = page_html.find_all('table')

df = pd.read_html(str(page_html))
del df[0]["Unnamed: 0"]
del df[0]["Unnamed: 4"]
del df[0]["Your Rating"]

df[0].to_csv("imdbtop.csv")
