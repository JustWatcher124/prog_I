b_a = int(input("Wie breit ist die Matrix a"))
h_a = int(input("Wie hoch ist die Matrix a"))
a = []
for y in range(h_a):
    reihe = []
    for x in range(b_a):
        reihe.append(int(input()))
    a.append(reihe)



b_b = int(input("Wie breit ist die Matrix b"))
h_b = int(input("Wie hoch ist die Matrix b"))
b = []
for y in range(h_b):
    reihe = []
    for x in range(b_b):
        reihe.append(int(input()))
    b.append(reihe)

print(a)
print(b)
c = []

for y in range(h_a):
    reihe = []
    for x in range(b_b):
        e = 0
        for i in range(h_b):
            e += a[y][x]*b[y][x]
        reihe.append(e)
    c.append(reihe)

print(c)