n = int(input())

# print all even numbers til n
i = 0
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

# print all odd numbers til n
j = 0
odd = 1
while j <= n:
    if j % 2 != 0:
        print(j)
    j += 1


# alternatively:
print("Even numbers:")
for i in range(0, n + 1, 2):
    print(i)

print("\nOdd numbers:")
for j in range(1, n + 1, 2):
    print(j)
