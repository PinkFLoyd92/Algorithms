class Team:
    name = ""
    wins  = 0
    ties = 0
    losses = 0
    def __init__(self,name):
        "docstring"
        self.name = name

        
    def get_total(self):
        return self.wins*3 + self.ties
        
    
