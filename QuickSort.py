# Encoding: UTF-8
# Authors: Irving Fuentes Aguilera, Roberto Téllez Perezyera

laLista = [0,1]
# [76,5,76,23,467,234,54,0,2,22]

def quickSort(lst, start, end):
    if start < end:
        pivot = quickSortPartition(lst, start, end)

        quickSort(lst, start, pivot - 1)
        quickSort(lst, pivot + 1, end)


def quickSortPartition(lst, start, end):
    pass