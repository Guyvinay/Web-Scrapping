import requests
from bs4 import BeautifulSoup
from statics import HEADERS

# Function to extract ByteCode of provided webpage
def scrapHtmlFromSite(url):
    
    try:
        #Passing User-Agent to bypass: 503 Service Unavailable Error
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Failed to scrape {url}:")
        return None

# Function to parse the ByteCode in the form of HTML
def parseHtmlWithBeautifulSoupe(html) :
    try:
        if html:
            return BeautifulSoup(html.content, 'html.parser')
        else:
            return None
    except Exception as e:
        print(f"Failed to parse HTML content:")
        return None