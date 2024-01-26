import requests
from bs4 import BeautifulSoup
from statics import HEADERS

def scrapHtmlFromSite(url):
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response
    except requests.RequestException as e:
        print(f"Failed to scrape {url}: {e}")
        return None

def parseHtmlWithBeautifulSoupe(html) :
    try:
        if html:
            return BeautifulSoup(html.content, 'html.parser')
        else:
            return None
    except Exception as e:
        print(f"Failed to parse HTML content: {e}")
        return None