#Python allows you to assign a single value to several variables simultaneously.
print('test 1')
a = b = c = 1

print(a)
print(b)
print(c)

#Here, an integer object is created with the value 1, and all the three variables are assigned to the same memory
# location. You can also assign multiple objects to multiple variables. For example −

print('test 2')
a, b, c = 1, 2, "john"

print(a)
print(b)
print(c)

print('test 3')
x = 11, 22, "Lime"

print('x=',x)