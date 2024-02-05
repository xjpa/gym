l = [1,2,3,4,5]
print(l) # [1, 2, 3, 4, 5]
print(l[3])# 4

# list functions
print(len(l)) # 5
l.append(155) # add value 155 to end
print(l) # [1, 2, 3, 4, 5, 155]
l.insert(1,69)
# insert "69" to index 1 and shift the rest to the right
print(l) # [1, 69, 2, 3, 4, 5, 155]
print(15 in l) # False -- because it doesnt exist there
print(l.count(2))  # 1 -- counting occurence of 30

# general purpose functions

print(l) # [1, 69, 2, 3, 4, 5, 155]
print('max', max(l)) # max 155
print('min', min(l)) # min 1
print('sum', sum(l)) # sum 239
l.reverse()
print('after reverse', l)
# after reverse [155, 5, 4, 3, 2, 69, 1]
l.sort()
print('after sorting', l)
# after sorting [1, 2, 3, 4, 5, 69, 155]