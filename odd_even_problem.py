num = int(input("Gib eine Zahl ein: "))
count = 0
while num != 4:
    if num % 2 == 0:
        num = num //2
    else:
        num = num * 3 + 1
    count += 1
    print(num)

print("Schritte bis 4:",count)