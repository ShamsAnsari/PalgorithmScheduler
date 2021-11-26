from Schedule import Schedule

class User:
    def __init__(self, name, userid, password): #Constructor
        self.name = name
        self.userid = userid
        self.password = password
        self.schedule = Schedule()
    
    def __eq__(self, other): #compares two users and returns True if they match
        return self.userid == other.userid

        
