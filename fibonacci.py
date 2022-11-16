n = int(input("Eine Obere Grenze für die Fibonacci Folge"))
f = [0,1]
while f[-1]+f[-2] <= n:
	f.append(f[-1]+f[-2])
for i in f:
    print(i,end=" ")