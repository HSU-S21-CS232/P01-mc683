import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=software+engineer&l=San+Francisco%2C+CA'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id= 'pageContent')

print(results)
