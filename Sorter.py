# Encoding: UTF-8
# Authors: Irving Fuentes Aguilera, Roberto Téllez Perezyera
"""
2nd term project for our Algorithms Analysis and Design course
"""

# import sys
# it = iter(sys.stdin.read().splitlines())
#
#
# lin = next(it).split(",")
# numbers = [int(x) for x in lin]     # list with inted numbers
# print(numbers)

"""
# una forma
x,y = 1,2
print(x,y)
x,y = y,x
print(x,y)

# la forma de luich
x, y = 3,4
print(x,y)
x += y
y = x-y
x -= y
print(x,y)
"""

laLista = [0,1,2,3,4,5,6]

def mergeSort(list):
    if len(list) == 1:
        return list
    elif len(list) == 2:
        # cases for 2 elems
        if list[0] > list[1]:
            list[0], list[1] = list[1], list[0]
            return list
        else:
            return list
    else:
        merge( mergeSort(list[0:len(list)//2]), mergeSort(list[len(list)//2:len(list)]) )

def merge(lst1, lst2):
    print(lst1, "manz")
    print(lst2, "ana")
    merged = [0]*(len(lst1) + len(lst2))

    print(len(merged))
    print((len(lst1) + len(lst2)))

    i = 0
    j = 0
    k = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2[j]:
            merged[k] = lst2[j]
            k += 1
            j += 1
        else:
            merged[k] = lst1[i]
            k += 1
            i += 1
    # exit while bc condition is no longer satisfied
    # one of the input arrays could still contain elems tho
    # traverse that array and insert them
    for m in range(i, len(lst1), 1):
        merged[k] = lst1[m]
        k += 1
    for m in range(j, len(lst2), 1):
        merged[k] = lst2[m]
        k += 1

    return merged


print(mergeSort(laLista))

