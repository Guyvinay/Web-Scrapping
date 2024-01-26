import json
import gzip

class Gzip :
    def __init__(self):
        pass

    def saveToGzip(self, laptops, city) :

        # Define the filename for the JSON file with city name
        filename = f'{city}.json'

        # Convert Laptop objects to list dictionary
        laptop_lists = []
        for laptop in laptops:

            laptop_dict = {
                "title": laptop.title,
                "price": laptop.price,
                "rating": laptop.rating,
                "description": laptop.description,
            }
            print(laptop_dict)

            laptop_lists.append(laptop_dict)

        # Open the JSON file in write 'w' mode and write the data
        with open(filename, 'w') as file:
            json.dump(laptop_lists, file, indent=4)