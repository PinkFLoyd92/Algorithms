# -*- coding: utf-8 -*-
class Team:
    name = ""
    wins  = 0
    ties = 0
    losses = 0
    goals = 0
    received_goals = 0
    def __init__(self,name):
        "docstring"
        self.name = name

        
    def get_total(self):
        return self.wins*3 + self.ties
        
    def __str__(self):
        return "Name: %s GOLES: %d GOLES RECIBIDOS: %d VICTORIAS: %d" %(self.name, self.goals, self.received_goals, self.wins)
