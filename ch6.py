class Athlete:
    
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    
    def top3(self):
        return(sorted(set([str(t) for t in self.times]))[0:3])