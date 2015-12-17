# -*- coding: utf-8 -*-
from tournament import Tournament
from tournament import mergeSort
from tournament import radixsort
from tournament import insertion_sort
from tournament import quickSort
from tournament import bubbleSort
from tournament import countingSort
from sys import argv

def radix_print(torneo):
    lista_numbers = []
    lista_radix = torneo.getLexicographicOrder()
    for item in lista_radix:
        lista_numbers.append(item[1])
        
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
    torneo.print_teams()
    print "----------------------------------"
    print "----------------------------------"
    print "QUICKSORT -- 1)Puntos Ganados"
    quickSort(torneo.teams)
    torneo.print_teams()
    print "----------------------------------"
    print "----------------------------------"
    print "Counting Sort -- 2)Partidos ganados"
    countingSort(torneo.teams, torneo.teams[-1].wins)
    torneo.print_teams()
    print "----------------------------------"
    print "----------------------------------"
    print "Buble Sort -- 3)Diferencia de Goles"
    bubbleSort(torneo.teams)
    torneo.print_teams()
    print "----------------------------------"
    print "----------------------------------"
    print "Merge Sort -- 4)Goles Marcados"
    mergeSort(torneo.teams)
    torneo.print_teams()
    print "----------------------------------"
    print "----------------------------------"
    print "Insertion Sort -- 5)Partidos Jugados"
    insertion_sort(torneo.teams)
    torneo.print_teams()
    print "----------------------------------"
    print "----------------------------------"
    print "Radix Sort -- 6)Orden lexicographic caso-no sensitivo"
    insertion_sort(torneo.teams)
    torneo.print_teams()
    
if __name__ == '__main__':
    main()
