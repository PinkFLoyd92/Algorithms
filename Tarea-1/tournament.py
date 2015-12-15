from sys import argv

class Tournament:
    teams = []
    matches= []
    filename=""
    def __init__(self,filename):
        self.filename = filename
        return
    def load_teams(self):
        f = open(self.filename, 'r')
        for line in f:
            print line,
    
