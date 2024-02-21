import requests
from bs4 import BeautifulSoup
from Constants import HEADERS


def runScrapperWithRequests(request_url):

    try : 
        response = requests.get(request_url, headers=HEADERS)
        return response
    except requests.RequestException as e :
        print(f"Request Failed to {request_url}")
        return

def parseContentWithBeautifulSoup(toBeParsed):

    try :
        return BeautifulSoup(toBeParsed.content, 'html.parser')
    except Exception as e : 
        print(f"Failed to Parse requested content!!!")
        return