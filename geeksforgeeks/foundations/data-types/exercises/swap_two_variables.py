# swap two variables' values

# a good approach is to have a temporary/temp variable
# to change one variable without losing reference to the other variable

x = 1
y = 2
print(x, y) # 1 2
temp = y
y = x
x = temp
print(x, y) # 2 1

# another trick, this time without using a temporary variagble

x = 1
y = 2
print(x, y) # 1 2
x, y = y, x
print(x, y) # 2 1

# alternatively in python we can do it with add/subtraction

x = 1
y = 2
print(x, y) # 1 2
x = x + y # 3
y = x - y # y is now 1
x = x - y # x is now 2
print(x, y) # 2 1
