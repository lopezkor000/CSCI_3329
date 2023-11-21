"""
Locations Class

    constructor:
    - list of locations (empty)
    - dictionary of categories (empty)
    
    functions:
    - add location
        [adds location to list of locations]

    - remove location
        [removes location in list of locations]

    - label location
        [includes location in category dict, labeling it]
"""

class Locations:
    def __init__(self):
        self.locations_list = []
        self.categories_dict = {}

    def add_location(self, location:str):
        self.locations_list.append(location)
        print(f"Location {location} added to the list.")

    def remove_location(self, location:str):
        if location in self.locations_list:
            self.locations_list.remove(location)
            print(f"Location {location} removed from the list.")
        else:
            print(f"Location {location} not found.")

    def label_location(self, location:str, category:str):
        if location in self.locations_list:
            if category in self.categories_dict:
                self.categories_dict[category].append(location)
            else:
                self.categories_dict[category] = [location]
            print(f"Location {location} labeled under category {category}.")
        else:
            print(f"Location {location} not found.")