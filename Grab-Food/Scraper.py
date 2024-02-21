from SoupParse import parseContentWithBeautifulSoup, runScrapperWithRequests
from Constants import BASE_URL
from Persist import Persist

class Scraper :
    def __init__(self):
        pass

    def main_scraper(self) : 

        extracted_restaurants = []

        persist = Persist()

        response  = runScrapperWithRequests(BASE_URL)

        soup_content = parseContentWithBeautifulSoup(response)

        restaurants = soup_content.find_all("div", attrs={"class":"RestaurantListCol___1FZ8V"})

        for rest in restaurants :

            restaurant_url = "https://food.grab.com"+rest.find('a').get('href')
            # print(restaurant_url)
            a_restaurant = runScrapperWithRequests(restaurant_url)

            a_restaurant_soup_content = parseContentWithBeautifulSoup(a_restaurant)

            merchant_info = a_restaurant_soup_content.find("div", attrs={"class":"merchantInfo___1GGGp"})

            merchant_photo_wrapper = a_restaurant_soup_content.find("img", attrs={"class":"realImage___2TyNE"})

            # print(merchant_photo_wrapper)

            restaurant_name = self.extract_restaurant_name(merchant_info)
            # print(restaurant_name)
            restaurant_cuisine = self.extract_restaurant_cuisine(merchant_info)

            restaurant_rating = self.extract_restaurant_rating(merchant_info)

            distance_from_location = self.extract_distance_from_location(merchant_info)

            delivery_time = self.extract_delivery_time(merchant_info)
            
            restaurant_dictionary = {
                "id":"restaurant.id",
                "restaurant_name":restaurant_name,
                "restaurant_cuisine":restaurant_cuisine,
                "restaurant_rating":restaurant_rating,
                "distance_from_location":distance_from_location,
                "delivery_time":delivery_time,
                "promotional_offers":"promotional_offers",
                "restaurant_image":"restaurant_image"
            }

            # promotional_offers = self.extract_promotional_offers(merchant_info)

            # restaurant_image = self.extract_restaurant_image(merchant_photo_wrapper)

            # restaurant_instance = Restaurant("", restaurant_name, restaurant_cuisine, restaurant_rating, delivery_time, distance_from_location, "promotional_offers", "restaurant_image")

            print(restaurant_dictionary)
            print()

            extracted_restaurants.append(restaurant_dictionary)

            persist.persistRestorantToJsonFile(extracted_restaurants)

        persist.persistRestorantToGZipFile(extracted_restaurants)

            # print(restaurant_name)
            # print(restaurant_cuisine)
            # print(restaurant_rating)
            # print(delivery_time)
            # print(distance_from_location)
            # print(promotional_offers)
            # print(restaurant_image)
            # print(extracted_restaurants)

    def extract_restaurant_cuisine(self, soup_content) : 

        ciusine = ""

        try :
            ciusine = soup_content.find("h3", attrs={"class":"cuisine___3sorn infoRow___3TzCZ"}).text.strip()
        except Exception :
            ciusine = ""

        return ciusine        

    def extract_restaurant_name(self, soup_content) :

        title = ""

        try :
            title = soup_content.find("h1", attrs={"class":"name___1Ls94"}).text.strip()
        except Exception :
            title = ""
        return title

    def extract_restaurant_rating(self, soup_content) : 

        rating = ""

        try :
            rating = soup_content.find("div", attrs={"class":"ratingAndDistance___1UT-a infoRow___3TzCZ"}).find("div", attrs={"class":"rating___1ZywF"}).text.strip()
        except Exception :
            rating = ""

        return rating  
    
    def extract_delivery_time(self, soup_content) : 

        time = ""

        try :
            time = soup_content.find("div", attrs={"class":"ratingAndDistance___1UT-a infoRow___3TzCZ"}).find("div", attrs={"class":"distance___3UWcK"}).text.split("•")[0].strip()
        except Exception :
            time = ""

        return time
    
    def extract_distance_from_location(self, soup_content) : 

        distance = ""

        try :
            distance = soup_content.find("div", attrs={"class":"ratingAndDistance___1UT-a infoRow___3TzCZ"}).find("div", attrs={"class":"distance___3UWcK"}).text.split("•")[1].strip()
        except Exception :
            distance = ""

        return distance
    
    def extract_promotional_offers(self, soup_content) : 

        offer = ""
        try :
            offer = soup_content.find("div", attrs={"class":"orderFeeMobile___3-tYC"}).text
        except Exception :
            offer = ""
        return offer

    def extract_restaurant_image(self, soup_content) : 
        image = ""
        try :
            image = soup_content.find("img", attrs={"class":"realImage___2TyNE show___3oA6B"})
            # print(image)
        except Exception :
            image = ""

        return image             