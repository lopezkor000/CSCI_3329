"""
Locations Class

    constructor:
    - list of locations (empty)
        
    functions:
    - add location
        [adds location to list of locations]

    - remove location
        [removes location in list of locations]

    - label location
        [includes location in category dict, labeling it]
"""
import csv

class Locations:
    def __init__(self, csvFile='locations.csv'):
        self.csvFile = csvFile
        self.locationsList = []  # 
        self.loadLocations()  # 

    def loadLocations(self):
        try:
            with open(self.csvFile, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    location = {
                        'Name': row['Name'],
                        'FoodType': row['FoodType']
                    }
                    self.locationsList.append(location)
        except FileNotFoundError:
            print(f"The file {self.csvFile} was not found. Creating a new one with default headers.")
            self.saveLocations()

    def saveLocations(self):
        with open(self.csvFile, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Name', 'FoodType']  # 
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for location in self.locationsList:
                writer.writerow(location)

    def addLocation(self, name, foodType):
        newLocation = {
            'Name': name,
            'FoodType': foodType
        }
        self.locationsList.append(newLocation)
        self.saveLocations()
        print(f"Location {name} added to the list.")

# Usage example
locations = Locations()  # This will automatically load data from 'locations.csv'
