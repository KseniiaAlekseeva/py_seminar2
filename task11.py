period = int(input("Enter period: "))

last_temp = 1
count = 0
mx_count = 0

for i in range(period):
    temp = int(input(f"{i} Enter temperature: "))
    if temp > 0:
        count += 1
        if i == period-1:
            if count > mx_count:
                mx_count = count
    else:
        if count > mx_count:
            mx_count = count
        count = 0

print(mx_count)
