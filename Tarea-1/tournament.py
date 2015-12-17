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

    def getTeam(self,name):
        for team in self.teams:
            if name == team.name:
                return team
        
    def getLexicographicOrder(self):
        lista_lexic = []
        score = "" #gettotal
        gamesplayed= "" # get_numberOfGames
        wins=""
        ties=""
        losses=""
        goal_difference = "" #get_goal_difference
        goals=""
        received_goals = ""
        
        for team in self.teams:
            if len(str(team.get_total()))==2:
                score = "0"+str(team.get_total())
            else:
                score = "00"+str(team.get_total())
                
            if len(str(team.get_numberOfGames()))==2:
                gamesplayed = "0"+str(team.get_numberOfGames())
            else:
                gamesplayed = "00"+str(team.get_numberOfGames())

            if len(str(team.wins))==2:
                wins = "0"+str(team.wins)
            else:
                wins = "00"+str(team.wins)
                
            if len(str(team.ties))==2:
                ties = "0"+str(team.ties)
            else:
                ties = "00"+str(team.ties)     

            if len(str(team.losses))==2:
                losses = "0"+str(team.losses)
            else:
                losses = "00"+str(team.losses)
                
            if len(str(team.goals))==2:
                goals = "0"+str(team.goals)
            else:
                goals = "00"+str(team.goals)
            lista_lexic.append([team.name,int(score+gamesplayed+wins+ties+losses+goals)])
        return lista_lexic

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
                # print(line)
               # next(f) #skip line
                index = [0,0]
                team_temp = []
                stats = []
            else: #if we get the correct line of scores.
                if(team_temp[0][1] >team_temp[1][1]):
                    if marcador[0] > marcador[1]:
                        stats.insert(0,[team_temp[1][0],1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],-1,marcador[1],marcador[0]])
                    elif marcador[0] == marcador[1]:
                        stats.insert(0,[team_temp[1][0],0,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],0,marcador[1],marcador[0]])
                    else:
                        stats.insert(0,[team_temp[1][0],-1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[0][0],1,marcador[1],marcador[0]])
                else:
                    if marcador[1] > marcador[0]:
                        stats.insert(0,[team_temp[0][0],-1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[1][0],1,marcador[1],marcador[0]])
                    elif marcador[0] == marcador[1]:
                        stats.insert(0,[team_temp[0][0],0,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[1][0],0,marcador[1],marcador[0]])
                    else:
                        stats.insert(0,[team_temp[0][0],1,marcador[0],marcador[1]])
                        stats.insert(1,[team_temp[1][0],-1,marcador[1],marcador[0]])
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
    print "merging.."

def radixsort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)
def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        # print a[i]
        j = i-1
        while j>=0 and a[j].get_numberOfGames() > key.get_numberOfGames():
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key
        
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = (alist[first].wins * 3) + (alist[first].ties)

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and (alist[leftmark].wins * 3) + (alist[leftmark].ties) <= pivotvalue:
            leftmark = leftmark + 1

        while (alist[rightmark].wins * 3) + (alist[rightmark].ties) >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

def countingSort( aList, k ):
    aList2 = list(aList)
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i.wins] += 1

    ndx = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        for j in aList2:
            if j.wins == i:
                temp = j
                aList2.remove(j)
                break
        aList[ndx] = temp
        ndx += 1
        counter[i] -= 1

def bubbleSort(alist):#goal difference
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i].get_goal_difference()>alist[i+1].get_goal_difference():
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
