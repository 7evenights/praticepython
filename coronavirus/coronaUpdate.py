from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"
r = requests.get(url).text

html_page = BeautifulSoup(r, "html.parser")
stat_table = html_page.find_all('table')

df = pd.read_html(str(html_page))

df[0].to_excel("coronaUpdate.xlsx")
