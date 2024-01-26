from statics import PINCODES, SEARCH_URL, MIN_CART_VALUE, HEADERS
from utility import scrapHtmlFromSite, parseHtmlWithBeautifulSoupe
from laptop import Laptop, Product
from gzips import Gzip

class Scrapper :

    def __init__(self):
        pass

    #Getting title from soupe
    def getTitle(self, soup):

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
    
    #Getting description from soupe
    def getDescription(self, soup):

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
    def getRating(self, soup):

        try:
            rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4 cm-cr-review-stars-spacing-big'}).string.strip()
        
        except AttributeError:
            try:
                rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
            except:
                rating = ""	

        return rating

    # Function to extract Product Price
    def getBrand(self, soup):

        try:
            price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()

        except AttributeError:

            try:
                # If there is some deal price
                price = soup.find("span", attrs={'id':'a-offscreen'}).string.strip()

            except:
                price = ""

        return price
    
        # Function to extract Product Price
   
    def getPrice(self, soup):

        try:
            price = soup.find("span", attrs={'class':'a-offscreen'}).string.replace('₹', '').strip()

        except AttributeError:

            try:
                # If there is some deal price
                price = soup.find("span", attrs={'id':'a-offscreen'}).string.replace('₹', '').strip()

            except:
                price = ""

        return price
    


    #Primary Function to exctract Laptps
    def laptops_scrapping(self):

        #Define a list to store Extracted Laptops
        laptops = []

        #Iterating cities
        for city, pincode in PINCODES.items() :

            #Url containing Pincode
            url = f"{SEARCH_URL}&pincode={pincode}"

            #Creating instance of Gzip to store laptops in gzip and Json file
            gZip = Gzip()

            # Making the HTTP request from Utility.py
            webpage = scrapHtmlFromSite(url)

            #Parsing webpage Html with BeautifulSoup from Utility
            soup = parseHtmlWithBeautifulSoupe(webpage)


            #Getting Links for all the Laptops by find_all()
            links = soup.find_all(
                "a",
                attrs={
                    "class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
                })

            d = {"title":"", "price":"", "rating":"","description":""}


            #Iterating through the Link and getting each laptop details
            for link in links :

                #Getting HTML for each Laptop
                new_webpage = scrapHtmlFromSite('https://www.amazon.in'+link.get('href'))

                #Getting Soup for each laptop
                new_soup = parseHtmlWithBeautifulSoupe(new_webpage)

                title = self.getTitle(new_soup)
                price = self.getPrice(new_soup)
                rating = self.getRating(new_soup)
                description = self.getDescription(new_soup)

                laptop = Product(title, price, rating, description)

                laptops.append(laptop)

                gZip.saveToGzip(laptops, city)

    #Run the main laptops_scrapping() function by Scrapper().runScrapper()
    def runScrapper(self):
        self.laptops_scrapping()