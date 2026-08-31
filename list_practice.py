list1 = [1, 2, 3]

list2 = list1

list2.append(4)

print(list1, id(list1))
print(list2, id(list2))


list1 = [1, 2, 3]

list2 = list1.copy()  # shallow copy

list2.append(4)

print(list1, id(list1))
print(list2, id(list2))


list = [37, 56, 67, 3, 67, 6, 3, 2, 3]

# print(min(list))
# print(max(list))
# print(list.count(67))

# list.sort()  # O (nlogn)
# print(list)

# list.reverse()  #o (n)
# print(list)

# print(list.index(3))
# print(list.index(56,2))

print(list[2:6:2])
print(list[2::2])
print(list[:2])
print(list[6:])
print(list[:])

print(list[::-1])