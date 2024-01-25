import requests
from bs4 import BeautifulSoup
from statics import HEADERS

def scrapHtmlFromSite(url):
    
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code == 200 :
        return response.content
    else :
        print(f"Failed Scrapping {url}")
        return None
    #  try:
    #     response = requests.get(url)
    #     return response.text
    # except requests.exceptions.RequestException as e:
    #     print(f"Failed to fetch HTML content from {url}: {e}")
    #     return None

def parseHtmlWithBeautifulSoupe(html) :
    return BeautifulSoup(html, 'html.parser')