# get the factorial
# e.g. 5!  = 5 * 4 * 3 * 2 * 1
n = int(input("give a number: "))

i = 1
factorial = 1
while i <= n:
    factorial *= i
    i += 1

print("factorial: ", factorial)