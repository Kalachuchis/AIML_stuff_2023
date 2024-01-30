import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

# invoke a get request
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")

# Find an HTML element by ID
results = soup.find(id="ResultsContainer")
# We can call prettify to organize the printed output
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # print(title_element.string)
    # print(company_element.string)
    # print(location_element.string)

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
# print(python_jobs)


python_job_elements = [
    job_element.parent.parent.parent for job_element in python_jobs
]
print(job_elements)
for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Link: {link_url}\n")
