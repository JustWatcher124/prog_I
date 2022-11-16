lim = int(input("Eine Obere Grenze für den das Sieb"))

isPrim = [False]*2 + [True]*(lim-2)
for i in range(2,lim):
    if not isPrim[i]:
        continue
    print(i)
    for k in range(i**2, lim, i):
        isPrim[k] = False

