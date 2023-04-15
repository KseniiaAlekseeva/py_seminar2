flag = False

while not flag:
    period = int(input("Enter period: "))
    if not (period < 1 or period > 100):
        flag = True

last_temp = 1
count = 0
mx_count = 0

for i in range(period):
    temp = int(input(f"{i} Enter temperature: "))
    if temp > 0:
        count += 1
    if i == period-1 or temp <= 0:
        if count > mx_count:
            mx_count = count
        count = 0

print(mx_count)
