import random
from backend.locations import Locations

class Selection:
    def __init__(self, numPeople):
        self.numPeople = numPeople
        self.locs = Locations()

    def totalRandom(self):
        if self.locs.listedLocs():
            return random.choice(self.locs.listedLocs())

    def categoryRandom(self, foodType):
        categoryLocations = [location for location in self.locs.listedLocs() if foodType in location]
        if categoryLocations:
            return random.choice(categoryLocations)