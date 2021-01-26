import requests

URL = 'https://www.indeed.com/jobs?q=software+engineer&l=San+Francisco%2C+CA'
page = requests.get(URL)
