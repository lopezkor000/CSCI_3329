
import random 

class Selection:
    def __init__(self, num_people): # of people choosing {passed in}

        self.num_people = num_people
        self.locations = []

    def select_mode(self, choice): # select mode [waits for user to pick category or totally random]
        if choice == "totally random":
            self.total_random()
        elif choice == "category random":
            self.category_random()
        else:
            print("Invalid choice.")

    def total_random(self): # total random [takes all locations saved and picks a random one]
        if self.locations:
            random_location = random.choice(self.locations)
            print(f"The totally random location is: {random_location}")
        else:
            print("No locations available.")

    def category_random(self): # category random [takes locations within label and picks a random one]
        label = input("Enter category label: ")
        category_locations = [location for location in self.locations if location.label == label] 
        if category_locations:
            random_location = random.choice(category_locations)
            print(f"The randomly chosen location from the category is: {random_location}")
        else:
            print(f"No locations available for the label {label}.")

    

# Usage:
# num_people = int(input("Enter the number of people choosing: "))
# selection_instance = Selection(num_people)
# selection_instance.select_mode()
# selection_instance.running_function(num_people)