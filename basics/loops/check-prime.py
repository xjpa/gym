# check if n is prime
n = int(input("enter number: "))

i = 1
count = 0
# find count of divisors
while i <= n:
    if n % i == 0:
        count += 1
    i += 1

# 2: prime numbers have 2 divisors, it's only divisble by itself and 1
if count == 2:
    print("prime")
else:
    print("nah")