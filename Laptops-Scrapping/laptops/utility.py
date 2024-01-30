import requests
from bs4 import BeautifulSoup
from statics import HEADERS
from retrying import retry


# Function to extract ByteCode of provided webpage
#@retry decorator/annotation to call again after failure
@retry(stop_max_attempt_number=2)
def scrapHtmlFromSite(url):
    
    try:
        #Passing User-Agent to bypass: 503 Service Unavailable Error
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Failed to Scrape!!!!\n{e}")
        return

# Function to parse the ByteCode in the form of HTML
def parseHtmlWithBeautifulSoupe(html) :
    try:
        if html:
            return BeautifulSoup(html.content, 'html.parser')
        else:
            return
    except Exception as e:
        print(f"Failed to parse HTML content:")
        return