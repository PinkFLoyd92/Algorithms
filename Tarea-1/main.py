# -*- coding: utf-8 -*-
from tournament import Tournament
from tournament import mergeSort
from sys import argv
def main():
    script, filename = argv
    txt = open(filename)
    torneo = Tournament(filename)
    torneo.load_teams()
    torneo.print_teams()
    mergeSort(torneo.teams)
    for team in torneo.teams:
        print team
        
if __name__ == '__main__':
    main()
