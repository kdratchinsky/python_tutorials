myint = 7
print(myint)

myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

a, b = 3, 4
print(a,b)

# tutorial 2
mystring = "hello"
myfloat = float(10)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)