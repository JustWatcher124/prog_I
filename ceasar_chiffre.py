text = input("Gebe ein Wort / Satz ein:").lower()#
s = int(input("Gebe eine Verschiebung ein: "))
def ceaser_chiffre(t,m):
    result = ""
    for i in range(len(t)):
        char = t[i]
        #if char != " ":
        result += chr((ord(char) + m - 97) % 26 + 97)
        #else:
         #   result += " "
    print(result)
ceaser_chiffre(text,-9)
print()
for i in range(26):
    print(i,end=":")
    ceaser_chiffre("gpkyfezjtffc", 26-i)
