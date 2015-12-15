from sys import argv
from team import Team
class Tournament:
    team_names = ["Emelec","River Ecuador","Ind. del Valle","Dep. Cuenca","Aucas","Dep. Quito","LDU Loja","LDU Quito", "Barcelona SC", "U. Católica","Mushuc Runa","El Nacional"]
    teams = []
    matches= []
    filename=""
    def __init__(self,filename):
        self.filename = filename
        for team_name in self.team_names:
            teams.append(Team(team_name))
        return
    def fill_team(self,stats):
        '''stats[0]->teamName,stats[1]->win=1,lose=-1,tie=0
        ,stats[2]->goals,stats[3]->received_goals'''
        for team in self.teams:
            if(stats[0]== team.name):
                if(stats[1])== 1:
                    team.wins = team.wins + 1
                if(stats[1])== 0:
                    team.ties = team.ties + 1
                if(stats[1])== -1:
                    team.losses = team.losses + 1
                team.received_goals = team.received_goals + stats[3]
                team.goals = team.goals + stats[2]

                    
    def load_teams(self):
        #indexes where the team was found.
        index = [0,0]
        team_1 = []
        team_2 = []
        indice_contador = 0
        f = open(self.filename, 'r')
        for line in f:
            # print line,
            for name in self.team_names:
                indice = line.find(name)
                if  indice != -1:
                    team_1[indice_contador] = [name,indice]
                    indice_contador= indice_contador + 1
            indice_contador = 0
                
