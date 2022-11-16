k, n, p = input("Gebe den Kredit, die Laufzeit und den Zinssatz (in %) ein (K L Z):").split(" ")
kredit, laufzeit, zinssatz = int(k), int(n), int(p)
tilgung = kredit/laufzeit
kredit_list = []
zins_list = []
annuitaet_list = []

for j in range(1,laufzeit+1):    
    zinsen = kredit * zinssatz/100
    annuitaet = zinsen + tilgung
    verbleibend = kredit - tilgung
    kredit_list.append(verbleibend)
    zins_list.append(zinsen)
    annuitaet_list.append(annuitaet)
    
    kredit = verbleibend

for i in range(len(kredit_list)):
    print(f"Im Jahr {i+1} ist der Kredit {kredit_list[i]}, die Zinsen {zins_list[i]}, ihre Tilgung {tilgung}. Ihre Annuität ist {annuitaet_list[i]} und der verbleibene Zins ist {verbleibend}")