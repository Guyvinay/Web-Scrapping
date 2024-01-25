from statics import PINCODES, SEARCH_URL, MIN_CART_VALUE, HEADERS
from utility import scrapHtmlFromSite, parseHtmlWithBeautifulSoupe
import requests
from bs4 import BeautifulSoup

class Scrapper :

    def __init__(self):
        pass


    def get_title(self, soup):

        try:
            # Outer Tag Object
            title = soup.find("span", attrs={"id":'productTitle'})
            
            # Inner NavigatableString Object
            title_value = title.text

            # Title as a string value
            title_string = title_value.strip()

        except AttributeError:
            title_string = ""

        return title_string

    def get_description(self, soup):

        try:
            # Outer Tag Object
            title = soup.find("span", attrs={"class":'a-list-item'})
            
            # Inner NavigatableString Object
            title_value = title.text

            # Title as a string value
            title_string = title_value.strip()

        except AttributeError:
            title_string = ""

        return title_string

    # Function to extract Product Rating
    def get_rating(self, soup):

        try:
            rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4 cm-cr-review-stars-spacing-big'}).string.strip()
        
        except AttributeError:
            try:
                rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
            except:
                rating = ""	

        return rating

    # Function to extract Product Price
    def get_price(self, soup):

        try:
            price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()

        except AttributeError:

            try:
                # If there is some deal price
                price = soup.find("span", attrs={'id':'a-offscreen'}).string.strip()

            except:
                price = ""

        return price



    def laptops_scrapping(self):

        url = f'https://www.amazon.in/s?k=laptop'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        # Make the HTTP request
        webpage = requests.get(url, headers=headers)

        soup = BeautifulSoup(webpage.content, "html.parser")

        links = soup.find_all("a",attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

        d = {"title":"", "price":"", "rating":"","description":""}

        for link in links :
            new_webpage = requests.get('https://www.amazon.in/'+link.get('href'), headers=headers)

            new_soup = BeautifulSoup(new_webpage.content, "html.parser")

            d['title'] = self.get_title(new_soup)
            d['price'] = self.get_price(new_soup)
            d['rating'] = self.get_rating(new_soup)
            d["description"] = self.get_description(new_soup)

            print(d)
            print()
            

    def runScrapper(self):
        self.laptops_scrapping()