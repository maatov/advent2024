import time

contents = open("input.txt").readlines()

list1 = sorted([int(line.split(" ")[0]) for line in contents])
list2 = sorted([int(line.strip().split(" ")[-1]) for line in contents])

# Part 1
result1 = sum([abs(n1 - n2) for n1, n2 in zip(list1, list2)])
print(result1)

# Part 2
result2 = sum([n * list2.count(n) for n in list1])
print(result2)
