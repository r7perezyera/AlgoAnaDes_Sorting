# Encoding: UTF-8
# Authors: Irving Fuentes Aguilera, Roberto Téllez Perezyera

laLista = [76,5,76,23,467,234,54,0,2,22]
# [76,5,76,23,467,234,54,0,2,22]

def quickSort(lst, start, end):
    if start < end:
        pivot = quickSortPartition(lst, start, end)

        quickSort(lst, start, pivot - 1)
        quickSort(lst, pivot + 1, end)


def quickSortPartition(lst, start, end):
    pivot = lst[end]
    i = (start - 1)
    for j in range(start, end, 1):
        if lst[j] <= pivot:
            i += 1
            # swap lst[i], lst[j]
            lst[i], lst[j] = lst[j], lst[i]     #hopefully this swap works as i think it does

    # swap lst[i+1], lst[end] (or pivot)
    lst[i+1], lst[end] = lst[end], lst[i+1]
    return i + 1

size = len(laLista)
quickSort(laLista, 0, size - 1)

result = ""
for i in range(0, size, 1):
    result += str(laLista[i]) + ", "
print(result[:-2])
