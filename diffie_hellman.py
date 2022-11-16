p = 257
e = 3
print("Lautsprecher:",p,e)
a = hash("ASecret")%(p-1)
x = e**a%p
print("Alice ruft:",x)
b = hash("BSecret")%(p-1)
y = e**b%p
print("Bob ruft:",y)

alice_s = y**a%p
bob_s = x**b%p

print("Alice berechnet:",alice_s)
print("Bob berechnet:",bob_s)

