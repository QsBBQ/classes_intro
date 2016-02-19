class Zoo(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.buildings = []

    def zoo_ledger(self):
        pass

    def add_building(self, building):
        self.buildings.append(building)

    def delete_building(self):
        pass
    def zoo_buildings(self):
        return self.buildings
