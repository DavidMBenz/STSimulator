class Starship:
    """
    Create starship object with power, population, and shield
    """
    def __init__(self, name: str):
        pass
        self.name = name
        self.power_min = 0
        self.power_max = 1000
        self.power_level = self.power_max
        self.population_min = 0
        self.population_max = 30
        self.population = self.population_min
        self.shield_min = 0
        self.shield_max = 100
        self.shield = self.shield_max

    def __str__(self):
        return 'This is the starship "' + self.name + '".'

    def __repr__(self):
        return 'name: ' + self.name + ', power: ' + str(self.power_level) + ', shield: ' + str(self.shield)  + ', pop: ' + str(self.population)


