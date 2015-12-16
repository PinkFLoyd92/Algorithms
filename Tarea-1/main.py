# -*- coding: utf-8 -*-
from tournament import Tournament
from sys import argv
def main():
    script, filename = argv
    txt = open(filename)
    torneo = Tournament(filename)
    torneo.load_teams()
    torneo.print_teams()
        
        
if __name__ == '__main__':
    main()
