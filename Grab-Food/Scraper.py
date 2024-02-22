from SoupParse import parseContentWithBeautifulSoup, runScrapperWithRequests
from Constants import BASE_URL
from Persist import Persist

#Main Scraper class to scrape restaurants
class Scraper :

    def __init__(self):
        pass

    #Main scraper method
    def main_scraper(self) : 

        #List to store scraped restaurants
        extracted_restaurants = []

        #creating instance of Persist class to persisit scraped data
        persist = Persist()

        #Sending request to grab-food
        response  = runScrapperWithRequests(BASE_URL)

        #Parsing the response from grab-food with BeautifulSoupe
        soup_content = parseContentWithBeautifulSoup(response)

        #Extracting the each restaurants link.
        restaurants = soup_content.find_all("div", attrs={"class":"RestaurantListCol___1FZ8V"})

        #Iterating over the links of all the restaurants
        for rest in restaurants :

            #appending 'https://food.grab.com' before the link to made it work
            restaurant_url = "https://food.grab.com"+rest.find('a').get('href')

            #to get id directly from the link
            url_contains_id = rest.find('a').get('href')

            # image = rest.find('a').find("div", attrs={"class":"placeholder___1xbBh"}).find("img")

            # print(image)

            #Sending request to each restaurants
            a_restaurant = runScrapperWithRequests(restaurant_url)

            #Parsing the response of each restaurants
            a_restaurant_soup_content = parseContentWithBeautifulSoup(a_restaurant)

            #Findind the div that contains the required restaurant details
            merchant_info = a_restaurant_soup_content.find("div", attrs={"class":"merchantInfo___1GGGp"})

            # photo = a_restaurant_soup_content.find("div", attrs={"class":"header___LAfE5"})

            # print(photo)

            #restaurant id
            restaurant_id = self.extract_restaurant_id(url_contains_id)

            #Restaurant Name
            restaurant_name = self.extract_restaurant_name(merchant_info)

            # print(restaurant_name)
            # restaurant_cuisine
            restaurant_cuisine = self.extract_restaurant_cuisine(merchant_info)

            # restaurant_rating
            restaurant_rating = self.extract_restaurant_rating(merchant_info)

            # distance_from_location
            distance_from_location = self.extract_distance_from_location(merchant_info)

            # delivery_time
            delivery_time = self.extract_delivery_time(merchant_info)
            
            # promotional_offers
            promotional_offers = self.extract_promotional_offers(merchant_info)

            # restaurant_image = self.extract_restaurant_image(merchant_photo_wrapper)
            # Creating a dictionary with required details of restaurant
            restaurant_dictionary = {
                "id":restaurant_id,
                "restaurant_name":restaurant_name,
                "restaurant_cuisine":restaurant_cuisine,
                "restaurant_rating":restaurant_rating,
                "distance_from_location":distance_from_location,
                "delivery_time":delivery_time,
                "promotional_offers":promotional_offers,
                "restaurant_image":"restaurant_image"
            }



            # restaurant_instance = Restaurant("", restaurant_name, restaurant_cuisine, restaurant_rating, delivery_time, distance_from_location, "promotional_offers", "restaurant_image")

            print(restaurant_dictionary)
            print()

            # appending scraped restaurant to list
            extracted_restaurants.append(restaurant_dictionary)

            #Persisting to json file
            persist.persistRestorantToJsonFile(extracted_restaurants)

            #Persisting to gzip file

            # print(restaurant_name)
            # print(restaurant_cuisine)
            # print(restaurant_rating)
            # print(delivery_time)
            # print(distance_from_location)
            # print(promotional_offers)
            # print(restaurant_image)
            # print(extracted_restaurants)
            
        persist.persistRestorantToGZipFile(extracted_restaurants)
        
    #Function to scrape restaurant_id
    def extract_restaurant_id(self, url_contains_id) : 

        id = url_contains_id.split("/")[-1].replace('?', '')
        return id        
        

    #function to extract restaurant_cuisine
    def extract_restaurant_cuisine(self, soup_content) : 

        ciusine = ""

        try :
            ciusine = soup_content.find("h3", attrs={"class":"cuisine___3sorn infoRow___3TzCZ"}).text.strip()
        except Exception :
            ciusine = "Cuisine Not Found"

        return ciusine        

    #Function to extract restaurant_name
    def extract_restaurant_name(self, soup_content) :

        title = ""

        try :
            title = soup_content.find("h1", attrs={"class":"name___1Ls94"}).text.strip()
        except Exception :
            title = "Name Not Found"
        return title

    #Function to extract restaurant_rating
    def extract_restaurant_rating(self, soup_content) : 

        rating = ""

        try :
            rating = soup_content.find("div", attrs={"class":"ratingAndDistance___1UT-a infoRow___3TzCZ"}).find("div", attrs={"class":"rating___1ZywF"}).text.strip()
        except Exception :
            rating = "Rating Not Found"

        return rating  
    
    #Function to extract delivery_time
    def extract_delivery_time(self, soup_content) : 

        time = ""

        try :
            time = soup_content.find("div", attrs={"class":"ratingAndDistance___1UT-a infoRow___3TzCZ"}).find("div", attrs={"class":"distance___3UWcK"}).text.split("•")[0].strip()
        except Exception :
            time = "Delivery Time Not found"

        return time
    
    #Function to extract distance from location
    def extract_distance_from_location(self, soup_content) : 

        distance = ""

        try :
            distance = soup_content.find("div", attrs={"class":"ratingAndDistance___1UT-a infoRow___3TzCZ"}).find("div", attrs={"class":"distance___3UWcK"}).text.split("•")[1].strip()
        except Exception :
            distance = "Distance Not Found"

        return distance
    
    #Function to extract promotional offers from restaurants
    def extract_promotional_offers(self, soup_content) : 

        offer = ""
        try :
            offer = soup_content.find("div", attrs={"class":"orderFeeContent___HyVYZ"}).text.strip()
        except Exception :
            offer = "Offer Not Found"   
        return offer
    
    #Functiont to scrape restaurants image
    def extract_restaurant_image(self, soup_content) : 
        image = ""
        try :
            image = soup_content.find("img", attrs={"class":"realImage___2TyNE show___3oA6B"})
            # print(image)
        except Exception :
            image = ""

        return image             