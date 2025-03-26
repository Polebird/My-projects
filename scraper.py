import requests
from bs4 import BeautifulSoup
import time

print("Enter a skill you are not familliar with")
unfamilliar_skill=input('>')
print(f'filtering out {unfamilliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml') 
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish=job.find('span', class_='sim-posted').span.text
        if 'few' in publish:
            company_name=job.find('h3',class_='joblist-comp-name').text
            role=job.find('h2', class_='heading-trun').text.replace(' ','')
            skill=job.find('div', class_='more-skills-sections').text
            more_info=job.header.h2.a['href']
            if unfamilliar_skill not in skill: 
                with open(f'C:\\Users\\asrso\\Documents\\scraper\\posts/{index}.txt','w') as f:
                    print(f"File Saved {index}")
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Role: {role.strip()}\n")
                    f.write(f"Required Skill: {skill}\n")
                    f.write(f"More Info: {more_info}")

if __name__  == '__main__':
      while True:
            find_jobs()
            time_wait=10
            print(f"Waiting {time_wait} minutes...")
            time.sleep(time_wait*60)