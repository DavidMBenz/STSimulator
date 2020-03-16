class Command:
    """
    Create command station object with score, crew limit, and list of crew.
    """
    def __init__(self):
        pass
        self.score = 30
        self.crew_cap = 6
        self.crew_list = []
        self.crew_num = len(self.crew_list)

    def __str__(self):
        return 'This is the command station.'

    def __repr__(self):
        return 'command station score: ' + str(self.score) + ', crew: ' + str(self.crew_num)

class Science:
    """
    Create science station object with score, crew limit, and list of crew.
    """
    def __init__(self):
        pass
        self.score = 30
        self.crew_cap = 6
        self.crew_list = []
        self.crew_num = len(self.crew_list)

    def __str__(self):
        return 'This is the science station.'

    def __repr__(self):
        return 'science station score: ' + str(self.score) + ', crew: ' + str(self.crew_num)

class Tactical:
    """
    Create tactical station object with score, crew limit, and list of crew.
    """
    def __init__(self):
        pass
        self.score = 30
        self.crew_cap = 6
        self.crew_list = []
        self.crew_num = len(self.crew_list)

    def __str__(self):
        return 'This is the tactical station.'

    def __repr__(self):
        return 'tactical station score: ' + str(self.score) + ', crew: ' + str(self.crew_num)

class Engineering:
    """
    Create engineering station object with score, crew limit, and list of crew.
    """
    def __init__(self):
        pass
        self.score = 30
        self.crew_cap = 6
        self.crew_list = []
        self.crew_num = len(self.crew_list)

    def __str__(self):
        return 'This is the engineering station.'

    def __repr__(self):
        return 'engineering station score: ' + str(self.score) + ', crew: ' + str(self.crew_num)

class Medical:
    """
    Create medical station object with score, crew limit, and list of crew.
    """
    def __init__(self):
        pass
        self.score = 30
        self.crew_cap = 6
        self.crew_list = []
        self.crew_num = len(self.crew_list)

    def __str__(self):
        return 'This is the medical station.'

    def __repr__(self):
        return 'medical station score: ' + str(self.score) + ', crew: ' + str(self.crew_num)

if __name__ == '__main__':
    Command()
    Science()
    Tactical()
    Engineering()
    Medical()
    
