
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

lst = [0,1,2,3,4,5,6]

leftHalf = lst[0:len(lst)//2]
rightHalf = lst[len(lst)//2:len(lst)]

print(leftHalf)
print(rightHalf)