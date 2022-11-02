
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
  
    return True


start, stop = input("Bitten gebe 2 Zahlen ein zwischen denen Primzahlen gesucht werden sollen (N N): ").split(" ")


for num in range(int(start), int(stop)):
    val = isPrime(num)
    
    if val:
        print("Primzahl:",num)
        l = int(str(num)[::-1])
        if isPrime(l):
            print("Die Spiegelzahl",l,"ist auch eine Primzahl")


