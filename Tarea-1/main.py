# -*- coding: utf-8 -*-
from tournament import Tournament
from tournament import mergeSort
from tournament import radixsort
from tournament import insertion_sort
from sys import argv

def radix_print(torneo):
    lista_numbers = []
    lista_radix = torneo.getLexicographicOrder()
    for item in lista_radix:
        lista_numbers.append(item[1])
        # print item[1]
        
    lista_numbers = radixsort(lista_numbers)
    for item in lista_numbers:
        for team in lista_radix:
            if team[1] == item:
                equipo = torneo.getTeam(team[0])
                print equipo

                
def main():
    script, filename = argv
    txt = open(filename)
    torneo = Tournament(filename)
    torneo.load_teams()
    insertion_sort(torneo.teams)
    torneo.print_teams()
    print "RADIX SORT"
    # radix_print(torneo)
    
if __name__ == '__main__':
    main()
