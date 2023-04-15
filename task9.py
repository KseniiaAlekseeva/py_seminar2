# n!

flag = False

while not flag:
    n = int(input("Enter positive integer: "))
    if (n >= 0):
        flag = True

i = 2
fact = 1

while i <= n:
    fact *= i
    i += 1

print(f"Factorial({n})={fact}")
