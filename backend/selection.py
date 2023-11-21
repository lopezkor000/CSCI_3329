"""
Selection Class
    constructor:
    - # of people choosing {passed in}

    functions:
    - select mode
        [waits for user to pick category or totally random]
    
    - total random
        [takes all locations saved and picks a random one]
    
    - category random
        [takes locations within label and picks a random one]
    
    - running function
        [recursively calls itself for as many people that are participating]
"""

import random
from locations import Locations  # Import the updated Locations class

class Selection:
    def __init__(self, numPeople):
        self.numPeople = numPeople
        self.locationsManager = Locations()  # Locations class to manage CSV data
        self.locations = self.locationsManager.locationsList  # Dictionaries from locations.csv

    def selectMode(self, choice):
        if choice == "totally random":
            self.totalRandom()
        elif choice == "category random":
            self.categoryRandom()
        else:
            print("Invalid choice.")

    def totalRandom(self):
        if self.locations:
            randomLocation = random.choice(self.locations)
            print(f"The totally random location is: {randomLocation['Name']}")
        else:
            print("No locations available.")

    def categoryRandom(self):
        foodType = input("Enter food type: ")  # category refers to 'FoodType'
        categoryLocations = [location for location in self.locations if location['FoodType'] == foodType]
        if categoryLocations:
            randomLocation = random.choice(categoryLocations)
            print(f"The randomly chosen location from the food type {foodType} is: {randomLocation['Name']}")
        else:
            print(f"No locations available for the food type {foodType}.")

# Usage
selection = Selection(numPeople=2)
selection.selectMode("totally random")
