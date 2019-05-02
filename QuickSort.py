# Encoding: UTF-8
# Authors:

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
            lst[i], lst[j] = lst[j], lst[i]

    # swap lst[i+1], lst[end] (or pivot)
    lst[i+1], lst[end] = lst[end], lst[i+1]
    return i + 1


def main():
    file = open("numbers.txt", "r")
    line = file.readline().split(",")
    file.close()

    numbers = []
    for string in line:
        numbers.append(int(string))

    size = len(numbers)
    quickSort(numbers, 0, size - 1)

    result = ""
    for i in range(0, size, 1):
        result += str(numbers[i]) + ", "
    print(result[:-2])

main()
