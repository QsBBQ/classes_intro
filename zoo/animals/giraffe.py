from zoo.animals.base_animal import Animal


class Giraffe(Animal):
    eats_per_day = 3
    animal_type = "Giraffe"
    
    def __init__(self, name):
        super(Giraffe, self).__init__(name)
