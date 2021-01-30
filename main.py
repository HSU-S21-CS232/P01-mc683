import requests
from bs4 import BeautifulSoup

job = input('Please enter a job to search for. If it is two words then put a hyphen in between: ')
where = input('What city would you like to work? If there is a space then please insert a hyphen: ')
state = input('Two characters for the state.')
URL = f'https://www.monster.com/jobs/search/?q={job}&where={where}__2C-{state.upper()}&intcid=skr_navigation_nhpso_searchMain'
page = requests.get(URL)

# using bs4 to parse the above url content. results variable to locate the html that houses all the jobs
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id= 'ResultsContainer')

# job_elems finds all the sections that have job info. For loop to go through whole page of jobs.
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):  #this was important because we keep running into an error dealing with no values.
        continue
    print(title_elem.text.strip())  #using strip on these to eliminate a lot of white space.
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

#print(results.prettify())