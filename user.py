from schedule import Schedule

class User:
    #Constructor
    def __init__(self, name, userid, password):
        self.name = name
        self.userid = userid
        self.password = password
        self.schedule = Schedule()
    
    #Equal to operator that returns true | compares two objects by their values which are users in this case and see if they equal to each other
    def __eq__(self, other):
        return self.userid == other.userid
	
    #Getters | More or less get the specific object
    def get_name(self):
        return self.name
	
    def get_userid(self):
        return self.userid

