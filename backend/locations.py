import csv

class Locations:
    def __init__(self):
        self.csvFile = 'locations.csv'
        self.loadLocations()

    def loadLocations(self):
        """
        Makes sure the CSV file exists, otherwise makes one
        """
        
        try:
            with open(self.csvFile, mode='r') as file:
                pass
        except FileNotFoundError:
            self.CreateCSV()

    def addLocation(self, name, *args):
        """
        Appends a new place to eat and adds appropriate categories
        """

        newLocation = [name, list(args)]
        with open(self.csvFile, mode='a', newline='') as file:
            csv.writer(file).writerow(newLocation)

    def CreateCSV(self):
        """
        Creates new empty CSV with headers to track our places to eat
        """

        with open(self.csvFile, mode='w', newline='') as file:
            fieldnames = ['Name', 'FoodType']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()