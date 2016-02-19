class Animal(object):
    # amount define in child class
    eats_per_day = None
    animal_type = None

    def __init__(self, name):
        self.name = name

    def feed_animals(self):
        """Feed my animals"""
        #each animals eats x amount of food
        # last time feed
        print('{0} the {1} just ate {2} units of food'.format(self.name, self.animal_type, self.eats_per_day))

    def food_cost(self, num_of_animals, per_animal_cost_per_day):
        """food cost per day"""
        # How to make it more friendly to change it per animal
        total_cost_per_day = num_of_animals * per_animal_cost_per_day
        return(total_cost_per_day)

    def inventory(self):
        """animal inventory"""
        # last count or rounds for inventory
        pass

    def animal_births(self):
        pass

    def animal_deaths(self):
        pass
