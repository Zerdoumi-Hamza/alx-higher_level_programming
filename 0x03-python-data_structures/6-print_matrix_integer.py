#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    lista = [row for row in matrix]
    for i in range(len(lista)):
        for j in lista[i]:
            print(j, end=' ')
        print()
