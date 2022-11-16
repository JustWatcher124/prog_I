import matplotlib.pyplot as plt
k, n, p = input("Gebe den Kredit, die Laufzeit und den Zinssatz (in %) ein (K L Z):").split(" ")
kredit, laufzeit, zinssatz = int(k), int(n), int(p)
zinsfaktor = 1 + zinssatz/100

kredit_list = [kredit]
zins_list = [0]
tilgung_list = [0]


annuitaet = kredit*(zinsfaktor**laufzeit * (zinsfaktor-1))/(zinsfaktor**laufzeit -1)
for j in range(1,laufzeit+1):    
    zinsen = kredit * zinssatz/100
    tilgung = annuitaet - zinsen
    verbleibend = kredit - tilgung
    kredit_list.append(verbleibend)
    zins_list.append(zinsen)
    tilgung_list.append(tilgung)
    #print(f"Im Jahr {j} ist der Kredit {kredit}, die Zinsen {zinsen}, ihre Tilgung {tilgung}. Ihre Annuität ist {annuitaet} und der verbleibene Zins ist {verbleibend}")
    kredit = verbleibend

for i in range(len(kredit_list)):
    print(f"Im Jahr {i} ist der Kredit {kredit_list[i]:6.2f}, die Zinsen {zins_list[i]:6.2f}, ihre Tilgung {tilgung_list[i]:6.2f}. Ihre Annuität ist {annuitaet:6.2f}5.")


jahre = [i for i in range(laufzeit+1)]

l = [[],[],[]]
l[0] = kredit_list 
l[1] = zins_list 
l[2] = tilgung_list

plt.plot(jahre,kredit_list)


plt.show()