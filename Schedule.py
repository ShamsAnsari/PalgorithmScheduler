class Schedule:
    def __init__(self): #Constructor
      self.events = []
    
    def add_event(self, event):
        self.events.append(event)
        self.events.sort()
    
    def delete_event(self, eventKey):
        for index in range(len(self.events)):
            if self.events[index].get_key() == eventKey:
                self.events.pop(index)
      
    def __getitem__(self, index): #Overloaded indexing [] operator.
        return self.events[index]
    
    def __str__(self):
        for ev in self.events: #Show schedule
            print(ev)

