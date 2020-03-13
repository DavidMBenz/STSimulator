class Station:
    """
    Create station object with power, population, and shield
    """
    def __init__(self):
        pass
        self.score = 30
        self.crew_num = 0
        self.crew_cap = 6

    def __str__(self):
        return 'This is a generic station.'

    def __repr__(self):
        return 'score: ' + str(self.score) + ', crew: ' + str(self.crew_num)

if __name__ == '__main__':
    unittest.main()