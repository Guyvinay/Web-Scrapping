from statics import PINCODES, SEARCH_URL, MIN_CART_VALUE, HEADERS
from utility import scrapHtmlFromSite, parseHtmlWithBeautifulSoupe
from laptop import Laptop, Product
from gzips import Gzip

#Scrapper class: Scrapping Laptop data from Amazon.in
class Scrapper :

    def __init__(self):
        pass

    #Getting title from soupe
    def getTitle(self, soup):

        try:
            # Outer Tag Object
            title = soup.find("div", attrs={"id":'title_feature_div'}).find('div', attrs={'id':'titleSection'}).find('h1', attrs={'id':'title'}).text.strip()

        except AttributeError:
            title = ""

        return title
    
    #Getting title from soupe
    def getImageUrl(self, soup):

        try:
            # Outer Tag Object
            imageUrl = soup.find("div", attrs={"id":'imgTagWrapperId'}).find('img').get('src')

        except AttributeError:
            imageUrl = ""

        return imageUrl
    

    #Getting Category from soupe
    def getCategory(self, soup):

        try:
            #Getting row of specs and values(tr)
            rows = soup.find("div", attrs={'class':'a-expander-content a-expander-section-content a-section-expander-inner'}).find('table', attrs={'id':'productDetails_techSpec_section_1'}).find_all('tr')

            #Iterating through each row
            for row in rows :

                th = row.find('th')
                #Checking if th contains Weight
                if th and th.text.strip() == 'Form Factor' :

                    #with tr getting value of Item Weight
                    category = row.find('td').text.strip()

        except AttributeError:
                
            category = ""

        return category

    #Getting countryOfOrigin from soupe
    def getCountryOfOrigin(self, soup):

        try:
            #Getting row of specs and values(tr)
            rows = soup.find("div", attrs={'class':'a-expander-content a-expander-section-content a-section-expander-inner'}).find('table', attrs={'id':'productDetails_techSpec_section_1'}).find_all('tr')

            #Iterating through each row
            for row in rows :

                th = row.find('th')
                #Checking if th contains Weight
                if th and th.text.strip() == 'Country of Origin' :

                    #with tr getting value of Item Weight
                    countryOfOrigin = row.find('td').text.strip()

        except AttributeError:
                
            countryOfOrigin = ""

        return countryOfOrigin
    
    def getSpecifications(self, soup):

        specs=""

        try:
            #Getting row of specs and values(tr)
            rows = soup.find("div", attrs={'class':'a-expander-content a-expander-section-content a-section-expander-inner'}).find('table', attrs={'id':'productDetails_techSpec_section_1'}).find_all('tr')

            #Iterating through each row
            for row in rows :

                th = row.find('th')
                #Checking if th contains Weight
                if th: 
                    if th.text.strip() == 'Processor Brand' or th.text.strip() == 'Processor Type' or th.text.strip() == 'Screen Resolution' or  th.text.strip() == 'Processor Speed'  or th.text.strip() == 'RAM Size' or th.text.strip() == 'Hard Drive Size'  or th.text.strip() == 'Operating System' or th.text.strip() == 'Connector Type' or th.text.strip() == 'Memory Technology'    :

                        #with tr getting value of Item Weight
                        specs = specs+row.find('td').text.strip()+", "

        except AttributeError:
                
            specs = ""

        return specs

    # Function to extract Product Rating
    def getRating(self, soup):

        try:
            rating = soup.find("div", attrs={'id':'averageCustomerReviews'}).find('i', attrs={'class':'a-icon a-icon-star a-star-4 cm-cr-review-stars-spacing-big'}).text.strip()
        
        except AttributeError:
            try:
                #Secondary
                rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4 cm-cr-review-stars-spacing-big'}).string.strip()
            except:
                rating = ""	

        return rating

    # Function to extract Product Price
    def getBrand(self, soup):

        try:
            #Getting row of specs and values(tr)
            rows = soup.find("div", attrs={'class':'a-expander-content a-expander-section-content a-section-expander-inner'}).find('table', attrs={'id':'productDetails_techSpec_section_1'}).find_all('tr')

            #Iterating through each row
            for row in rows :

                th = row.find('th')
                #Checking if th contains Weight
                if th and th.text.strip() == 'Brand' :

                    #with tr getting value of Item Weight
                    brand = row.find('td').text.strip()

        except AttributeError:
                
            brand = ""

        return brand
    
    def getModel(self, soup):

        try:
            model = soup.find('div', attrs={'class':'a-section a-spacing-small a-spacing-top-small'}).find('table',attrs={'class':'a-normal a-spacing-micro'}).find('tr', attrs={'class':'a-spacing-small po-model_name'}).find('span',attrs={'class':'a-size-base po-break-word'}).string.strip()

        except AttributeError:

            try:
                # Secondary Script
                model = soup.find('div', attrs={'class':'a-section a-spacing-small a-spacing-top-small'}).find('table',attrs={'class':'a-normal a-spacing-micro'}).find('tr', attrs={'class':'a-spacing-small po-model_name'}).find('span',attrs={'class':'a-size-base po-break-word'}).string.strip()

            except:
                model = ""

        return model

    # Function to extract Product Price
    def getSellingPrice(self, soup):

        try:
            price = soup.find("span", attrs={'class':'a-offscreen'}).string.replace('₹', '').strip()
            
        except AttributeError:

            try:
                # Secondary attributes after getting exception in first one
                price = soup.find("span", attrs={'class':'a-offscreen'}).string.replace('₹', '').strip()

            except:
                price = ""

        return price
    
    def getMarketRetailPrice(self, soup):

        try:
            price = soup.find("div", attrs={'class':'a-section a-spacing-small aok-align-center'}).find('span', attrs={'class':'a-price a-text-price'}).find('span', attrs={'class':'a-offscreen'}).string.replace('₹', '').strip()

        except AttributeError:

            try:
                # If there is some deal price
                price = soup.find("div", attrs={'class':'a-section a-spacing-small aok-align-center'}).find('span', attrs={'class':'a-price a-text-price'}).find('span', attrs={'class':'a-offscreen'}).string.replace('₹', '').strip()

            except:
                price = ""

        return price
    
    def getDiscount(self, soup):

        try:
            discount = soup.find("div", attrs={'id':'corePriceDisplay_desktop_feature_div'}).find('span', attrs={'class':'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).text.strip()

        except AttributeError:
                
            discount = ""

        return discount
    
    def getWeight(self, soup):
        try:
            #Getting row of specs and values(tr)
            rows = soup.find("div", attrs={'class':'a-expander-content a-expander-section-content a-section-expander-inner'}).find('table', attrs={'id':'productDetails_techSpec_section_1'}).find_all('tr')

            #Iterating through each row
            for row in rows :

                th = row.find('th')
                #Checking if th contains Weight
                if th and th.text.strip() == 'Item Weight' :

                    #with tr getting value of Item Weight
                    weight = row.find('td').text.strip()

        except AttributeError:
                
            weight = ""

        return weight
    
    

    #Primary Function to exctract Laptps
    def laptops_scrapping(self):

        #Define a list to store Extracted Laptops
        laptops = []

        #Iterating cities
        for city, pincode in PINCODES.items() :

            #Url containing Pincode
            url = f"{SEARCH_URL}&pincode={pincode}"

            print(url)

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

                # title = self.getTitle(new_soup)
                # sellingPrice = self.getSellingPrice(new_soup)
                # rating = self.getRating(new_soup)
                # discount = self.getDiscount(new_soup)
                # category = self.getCategory(new_soup)
                # brand = self.getBrand(new_soup)
                # model = self.getModel(new_soup)
                # mrp = self.getMarketRetailPrice(new_soup)
                # weight = self.getWeight(new_soup)
                # countryOfOrigin = self.getCountryOfOrigin(new_soup)
                # specifications = self.getSpecifications(new_soup)
                imageUrl = self.getImageUrl(new_soup)

                # print(title)
                # print(sellingPrice)
                # print(discount)
                # print(rating)
                # print(category)
                # print(brand)
                # print(model)
                # print(mrp)
                # print(weight)
                # print(countryOfOrigin)
                # print(specifications)
                print(imageUrl)
                print()
                # laptop = Product(title, price, rating, description)

                # laptops.append(laptop)

                # gZip.saveToGzip(laptops, city)

    #Run the main laptops_scrapping() function by Scrapper().runScrapper()
    def runScrapper(self):
        self.laptops_scrapping()