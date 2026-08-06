a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))

if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    print("a is the largest number")
elif b >= a and b >= c:
    print("b is the largest number")
else:
    print("c is the largest number")