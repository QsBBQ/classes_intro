import zoo.animals as Animals


class Monkey(Animals):
    def __init__(self, name):
        super(Monkey, self).__init__(name)

    def monkey_food_cost(self):
        """Food per day the monkeys need"""
        return 5
