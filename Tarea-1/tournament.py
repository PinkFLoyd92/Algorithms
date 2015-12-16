# -*- coding: utf-8 -*-
#pylint: disable-msg=too-many-arguments
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
            self.teams.append(Team(team_name))

    def print_teams(self):
        for team in self.teams:
            print(team)
            
        
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
        team_temp = [] # [[equipo1,indice inicial], [equipo2, indice inicial]]
        marcador = [] #[score_team1, score_team2]
        stats = [] #stats from 2 teams
        indice_contador = 0
        f = open(self.filename, 'r')
        for line in f:
            stats = []
            index = [0,0]
            team_temp = []
            # print line,
            for name in self.team_names:
                indice = line.find(name)
                if  indice != -1:
                    # team_temp[indice_contador] = [name,indice]
                    team_temp.insert(indice_contador, [name,indice])
                    indice_contador= indice_contador + 1
            indice_contador = 0
            marcador = [int(s) for s in line.split() if s.isdigit()]
            if len(marcador) !=2:
                print(line)
               # next(f) #skip line
                index = [0,0]
                team_temp = []
                stats = []
            else: #if we get the correct line of scores.
                if(team_temp[0][1] >team_temp[1][1]):
                    if marcador[0] > marcador[1]:
                        stats.insert(0,[team_temp[1][0],1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],-1,marcador[1],marcador[0]])
                    if marcador[0] == marcador[1]:
                        stats.insert(0,[team_temp[1][0],0,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],0,marcador[1],marcador[0]])
                    else:
                        stats.insert(0,[team_temp[1][0],-1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],1,marcador[1],marcador[0]])
                else:
                    if marcador[1] > marcador[0]:
                        stats.insert(0,[team_temp[1][0],1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],-1,marcador[1],marcador[0]])
                    if marcador[0] == marcador[1]:
                        stats.insert(0,[team_temp[1][0],0,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],0,marcador[1],marcador[0]])
                    else:
                        stats.insert(0,[team_temp[1][0],-1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],1,marcador[1],marcador[0]])
                    self.fill_team(stats[0])
                    self.fill_team(stats[1])
        f.close()        

def mergeSort(teams):
    if len(teams)>1:
        mid = len(teams)//2
        lefthalf = teams[:mid]
        righthalf = teams[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].goals < righthalf[j].goals:
                teams[k]=lefthalf[i]
                i=i+1
            else:
                teams[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            teams[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            teams[k]=righthalf[j]
            j=j+1
            k=k+1
    print "Merging..."

