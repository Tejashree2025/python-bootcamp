name = "physics teacher"

name+= "teaching"

print(len(name))
print(name[4])
print(name[-2])
print(type(name))

print(name.lower())
print(name.capitalize())
print(name.upper())
print(name.replace("i","z"))
s = "hello made"
print(s*3)

print(s.startswith("hello"))
print(s.endswith("hello"))
print(s.startswith("made"))
print(s.endswith("made"))
print(s.index("made"))
print(s.index("o made"))
print(name[2:6])
print(name[2:9:2])
print(list(s))

t ="    Teju  M   "
print(t.strip())


t1 ="--------python skills-------"
print(t1.strip("-"))

print(t.split(" "))

list =['a','b','h','i']

print("".join(list))

print("Hi\nWelcome")
print("Hi\tWelcome")

print(ord('t')) # to get ascii value of character