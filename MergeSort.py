# Encoding: UTF-8
# Authors: Irving Fuentes Aguilera, Roberto Téllez Perezyera

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
    merged = [0]*(len(lst1) + len(lst2))

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


def main():
    line = open("numbers.txt", "r").readline().split(",")

    numbers = []
    for string in line:
        numbers.append(int(string))

    ans = mergeSort(numbers)
    print(ans)

main()
