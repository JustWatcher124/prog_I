k, n, p = input("Gebe den Kredit, die Laufzeit und den Zinssatz (in %) ein (K L Z):").split(" ")
kredit, laufzeit, zinssatz = int(k), int(n), int(p)
tilgung = kredit/laufzeit
for j in range(1,laufzeit+1):    
    zinsen = kredit * zinssatz/100
    annuitaet = zinsen + tilgung
    verbleibend = kredit - tilgung
    print(f"Im Jahr {j} ist der Kredit {kredit}, die Zinsen {zinsen}, ihre Tilgung {tilgung}. Ihre Annuität ist {annuitaet} und der verbleibene Zins ist {verbleibend}")
    kredit = verbleibend