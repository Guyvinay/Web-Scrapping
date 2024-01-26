import json
import gzip

#Gzip class is for persisting scrapped data in ndjson.gz and Json files
class Gzip :

    def __init__(self):
        pass


    #Function to save data
    def saveToGzip(self, laptops, city) :

        # Define the filename for the JSON and ndjson files with city name
        jsonFileName = f'{city}.json'
        gzFileName = f'{city}.ndjson.gz'

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

            # Save to ndjson format
            with gzip.open(gzFileName, 'wt') as f:
                f.write(json.dumps(laptop_dict) + '\n') 
        

        # Open the JSON file in write 'w' mode and write the data
        with open(jsonFileName, 'w') as file:
            json.dump(laptop_lists, file, indent=4)