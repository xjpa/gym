'''
id

id function gives a unique identiifer for every object

basically id in python gives you the address of the object, like pointers in C/C++
'''

print(id(5))
a = 1
b = a
print(id(a))
print(id(b)) # will print the same value as a
a = 5
print(id(a)) # a has now a new value
print(id(b)) # b still printing the same value as it did before a was changed

# in python, literals if they ahve the same value, will be stored in the same location
c = 1
d = 1
# thus...
print("c:", id(c), "d:", id(d)) # both the id() on c and d will print the same value