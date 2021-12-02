import datetime
import uuid

class Event:
    def __init__(self, name, day, start, end, description):
        self.name = name
        
        self.start = start
        self.end = end
        self.key = str(uuid.uuid4())

        start = start.split(':')
        end = end.split(':')
        start = tuple(map(int, start))
        end = tuple(map(int, end))

        day = {'sunday' : 1, 'monday' : 2, 'tuesday' : 3, 'wednesday' : 4, 'thursday' : 5, 'friday' : 6, 'saturday' : 7, 'm' : 2}[day.lower()]

        self.day = day
        self.time = datetime.datetime(1, 1, day, start[0], start[1], 0)
    
    def __str__(self):
        return str(self.time)
    
    def __lt__(self, other):
        return self.time < other.time
    
    def get_key(self):
        return self.key
