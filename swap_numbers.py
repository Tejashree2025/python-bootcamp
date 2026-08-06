# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))

# temp = a
# a = b
# b = temp

# print("After swapping:")
# print("a =", a)
# print("b =", b)

'This is called tuple unpacking (or multiple assignment) in Python. Its one of Pythons most useful features.'

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

a, b = b, a

print("a =", a)
print("b =", b)