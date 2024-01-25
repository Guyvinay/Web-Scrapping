from statics import AMAZON_URL, PINCODES, SEARCH_URL, MIN_CART_VALUE, HEADERS
from utility import scrapHtmlFromSite, parseHtmlWithBeautifulSoupe


class Scrapper :
    def __init__(self):
        pass

    def laptops_scrapping(self):

        for city, pincode  in PINCODES.items():
            search_url = f"{SEARCH_URL}&pincode={pincode}"
            htmlContent = scrapHtmlFromSite(search_url)
            print(parseHtmlWithBeautifulSoupe(htmlContent))


    def runScrapper(self):
        self.laptops_scrapping()