'''
is
is opeerator checks if the identities of 2 operands are same or not
'''

a = 10
b = 10
print(a is b) # True as a and b refer to the same literal

c = a
print(c is b) # True

c = 20
print(c is b) # False
