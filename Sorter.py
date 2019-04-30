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

laLista = [76,5,76,23,467,234,54,0,2,22]

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            return lst
        else:
            return lst
    else:
        return merge( mergeSort(lst[0:len(lst) // 2]), mergeSort(lst[len(lst) // 2:len(lst)]) )

def merge(lst1, lst2):
    print("lH",lst1)
    print("rH",lst2)
    merged = [0]*(len(lst1) + len(lst2))
    print("merged",merged)
    print("lenMerged",len(merged))
    print("globalLen",(len(lst1) + len(lst2)))

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

