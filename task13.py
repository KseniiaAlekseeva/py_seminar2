from random import randint

n = randint(1, 10)
print(f"Total number of watermelons is {n}")

max_m = 100
min_m = 30000
for i in range(n):
    m = randint(100, 30000)
    print(f"Watermelon {i+1} mass - {m} g")
    if m > max_m:
        max_m = m
    if m < min_m:
        min_m = m
print(f"Min mass watermelon is {min_m}")
print(f"Max mass watermelon is {max_m}")
