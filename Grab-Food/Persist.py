import json
import gzip


class Persist :

    def __init__(self) -> None:
        pass

    gzipFileName = 'restaurants.gz'
    jsonFileName = 'restaurants.json'

    def persistRestorantToJsonFile(self, restaurants) :

        with open(self.jsonFileName, 'w') as file:
            json.dump(restaurants, file, indent=4)
    
    def persistRestorantToGZipFile(self, restaurant) :

        with gzip.open(self.gzipFileName, 'wt', encoding='utf-8') as f:
            json_entry = json.dumps(restaurant)
            f.write(json_entry + '\n')

    # Function to read and parse gzip file
    def read_gzip_file(self):
        data = []
        with gzip.open(self.gzipFileName, 'rt', encoding='utf-8') as f:
            for line in f:
                # Parse JSON from each line and append to data list
                data.append(json.loads(line))
        return data
