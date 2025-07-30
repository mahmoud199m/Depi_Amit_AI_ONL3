import requests
from bs4 import BeautifulSoup
 
html_text = requests.get(
    'https://wuzzuf.net/search/jobs?a=spbg&q=machine%20learning')
 
soup = BeautifulSoup(html_text.text, 'lxml')
jobs = soup.find_all('div', class_ ='css-1gatmva e1v1l3u10')

for job in jobs:
    
    location_date = job.find('div', class_ ='css-d7j1kk')
    company_name = location_date.a
    skills = job.find('div', class_ ='css-y4udm8')
    if job ==jobs[0] :
        date = job.find('div', class_ ='css-4c4ojb')
    else :date = job.find('div', class_ ='css-do6t5g')
 
    if company_name and skills and location_date :
        company_name = company_name.text.strip().replace('-','')
        skills = ''.join(skill.strip() for skill in skills.text.strip().split('.'))
        location_date = location_date.span.text.strip()
        if date:
            date = date.text.strip()
 
    print(f'''  
Company Name     : {company_name}
Location   : {location_date}
Date   : {date}
Required Skills  : {skills}
    ''')
    print("="*50)
 
 