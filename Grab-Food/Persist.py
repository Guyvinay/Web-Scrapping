import json


class Persist :
    
    def __init__(self) -> None:
        pass

    def persistRestorantToJsonFile(self, restaurants) :

        jsonFileName = 'restaurants.json'

        with open(jsonFileName, 'w') as file:
            json.dump(restaurants, file, indent=4)
