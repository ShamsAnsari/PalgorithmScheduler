import datetime
import uuid

class Event:
    def __init__(self, name, day, start, end, description):
        self.name = name
        self.day = day
        self.start = start
        self.end = end
        self.key = str(uuid.uuid4())
        self.time = datetime.datetime(1, 1, day, start[0], start[1], 0)
    
    def __str__(self):
        return str(self.time)
    
    def __lt__(self, other):
        return self.time < other.time
    
    def get_key(self):
        return self.key
