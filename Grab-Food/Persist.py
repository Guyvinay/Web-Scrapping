import json
import gzip

#Persist Class to Persist the extracted data to Gz and  json files
class Persist :

    def __init__(self) -> None:
        pass

    #Files name to persist data
    gzipFileName = 'restaurants.gz'
    jsonFileName = 'restaurants.json'

    #TO persist retrieved data to json file, takes all restairants as argument
    def persistRestorantToJsonFile(self, restaurants) :

        #Open the json file in write mode as file
        with open(self.jsonFileName, 'w') as file:
            #Serialize restaurants to Json form and persist
            json.dump(restaurants, file, indent=4)
    
    #To Persist data to gzip file, takes a resturant as argument
    def persistRestorantToGZipFile(self, restaurant) :

        #open with gzip in wt mode as file f
        with gzip.open(self.gzipFileName, 'wt', encoding='utf-8') as f:

            #Serialize restauran to json form before persist
            json_entry = json.dumps(restaurant)
            #write serialized data to f
            f.write(json_entry + '\n')

    #to read gzip file
    def read_gzip_file(self):
        data = []
        #open gzip file in read text mode
        with gzip.open(self.gzipFileName, 'rt', encoding='utf-8') as f:
            for line in f:
                # deserialize the restaurant and store in data
                data.append(json.loads(line))
        return data
