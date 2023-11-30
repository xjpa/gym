# type()
# built-in function that returns the data type of a variable/value

a = 10
print(type(a)) # int

b = 10.5
print(type(b)) # float

c = 2 + 4j # complex number
print(type(c)) # complex

# sequence types (collections)

str = "John"
print(type(str)) # str

l = [10, 20, 30]
print(type(l)) # list
# like arrays in other languages,
# but with python we can dynamically add/remove items
# so its kinda like arraylist in java or vector in C++


t = (10, 20, 30)
print(type(t)) # tuple
# like a list but it's immutable, we cant modify/add/remove items

s = {10, 20, 30}
print(type(s)) # set
# curly brackets for sets
# dynamically sized collection of distinct items
# fast operations, internally uses hashing to implement the (distinct) keys

d = {10: "a", 20: "b"}
print(type(d)) # dict
# dictionaries are used to store mappings and key-value pairs
