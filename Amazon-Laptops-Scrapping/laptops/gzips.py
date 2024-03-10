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
        gzFileName = f'{city}.gzip'

        # Convert Laptop objects to list dictionary
        laptop_lists = []
        for laptop in laptops:          
            #Creating dictionary of Laptop object
            laptop_dict = {
                "id":laptop.id,
                "name":laptop.name,
                "title": laptop.title,
                "model": laptop.model,
                "description": laptop.description,
                "category": laptop.category,
                "mrp": laptop.mrp,
                "sellingPrice":laptop.sellingPrice,
                "discount":laptop.discount,
                "weight":laptop.weight,
                "brandName": laptop.brandName,
                "imageUrl": laptop.imageUrl,
                "specifications": laptop.specifications,
                "rating": laptop.rating,
                "countryOfOrigin": laptop.countryOfOrigin,
            }

            print(laptop_dict)
            print()

            #Saving the laptop_dict t list
            laptop_lists.append(laptop_dict)

            # Save to ndjson format
            with gzip.open(gzFileName, 'wt') as f:
                f.write(json.dumps(laptop_dict) + '\n') 
        

        # Open the JSON file in write 'w' mode and write the laptop_lists data
        with open(jsonFileName, 'w') as file:
            json.dump(laptop_lists, file, indent=4)
#End of Persisting scrapped data in files            