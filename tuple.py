tuple1 = (1, 2, 3, 4, 5, "Hello", 567.89,5,5,5,5,5,5,5)

tuple2 = tuple1

print(tuple2)

print(len(tuple1))
print(type(tuple1))

print(tuple1[-5])

print(tuple1[6])

print(tuple1[2:6])


print(tuple1.index(5))


print(tuple1.count(5))


#convert tuple to list

list1 = list(tuple1)

print(list1)
