'''
variables - used to store data in memory

python is DYNAMICALLY typed, meaning variables are just references to memory locations, there is no type info associated with them

None -- special value in python when youre not sure what to assign it with or to reset the variable
'''

price = 100
# the memory location for the value 100 is created, and we use 'price' as a reference to this location
tax = 10
total_price = price + tax
print(total_price) #110
z = tax
# z becomes a reference to the same location as the value that tax is referencing, thus z = 10
print(z)
tax = 100
print(tax) # 100
print(z) # 10
print(tax, z) # prints: 100 10