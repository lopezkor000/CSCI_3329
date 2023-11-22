import csv
# edit
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

        newLocation = [x for x in args]
        newLocation.insert(0, name)
        with open(self.csvFile, mode='a', newline='') as file:
            csv.writer(file).writerow(newLocation)
    
    def removeLocation(self, name):
        """
        Looks for first instance of location then recreates CSV without it
        """
        
        locs = self.listedLocs()
        for i, loc in enumerate(locs):
            if loc[0] == name:
                locs.pop(i)
                break
        self.CreateCSV(locs)

    def CreateCSV(self, locs=None):
        """
        Creates new empty CSV with headers to track our places to eat
        """

        with open(self.csvFile, mode='w', newline='') as file:
            writer = csv.writer(file)
            if locs != None:
                for loc in locs:
                    writer.writerow(loc)
    
    def listedLocs(self) -> list:
        """
        Returns listed rows of locations in CSV
        """

        with open(self.csvFile, mode='r') as file:
            return [place for place in csv.reader(file)]