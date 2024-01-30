import os
import pandas as pd

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    URL = "https://pythonjobs.github.io"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    main_container = soup.find(id="content")
    job_list = main_container.find_all("div", class_="job")
    jobs = {}
    for job_element in job_list:
        job_title = job_element.find("h1").string
        job_link = URL + job_element.find("a", class_="go_button")["href"]
        job_info = job_element.find_all("span", class_="info")
        job_posting_date = job_info[1].text
        job_company = job_info[3].text
        job_contract_type = job_info[2].text
        job_page = requests.get(job_link)

        attributes = {
            "Posting Date": job_posting_date,
            "Company Name": job_company,
            "Contract Type": job_contract_type,
            "HTML": job_page,
        }

        jobs[job_title] = attributes

    folder = 'skills'
    pattern = "\w+"
    for job in jobs.keys():
        job_soup = BeautifulSoup(jobs[job]["HTML"].content, "html.parser")
        job_content = job_soup.find("article", class_="job")
        job_tags_list = job_content.find("div", class_="tags").text.split()

        job_contact_info_all = job_soup.find_all("div", class_="field")
        job_contact_person = job_contact_info_all[0].text.split()[1]
        job_company_email = job_contact_info_all[1].text.split()[1]
        job_company_website = job_contact_info_all[2].text.split()[1]

        overview = (job_soup.find("div", class_="body"))
        overview_text = overview.find('p').text

        jobs[job]['Company Contact Name'] = job_contact_person
        jobs[job]['Company Email'] = job_company_email
        jobs[job]['Company Website'] = job_company_website
        jobs[job]['Skills Tag'] = job_tags_list

        company_folder = os.path.join(folder, jobs[job]['Company Name'])
        try:

            os.makedirs(company_folder)
        except FileExistsError:
            pass

        with open(f'{company_folder}/overview_{job}.txt', 'w', encoding='utf-8') as f:
            f.write(overview_text)

    df = pd.DataFrame.from_dict(jobs, orient='index')
    df.to_csv('exercise.csv')
    
    print(df)


