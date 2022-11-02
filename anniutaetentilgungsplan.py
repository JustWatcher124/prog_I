k, n, p = input("Gebe den Kredit, die Laufzeit und den Zinssatz (in %) ein (K L Z):").split(" ")
kredit, laufzeit, zinssatz = int(k), int(n), int(p)
zinsfaktor = 1 + zinssatz/100

annuitaet = kredit*(zinsfaktor**laufzeit * (zinsfaktor-1))/(zinsfaktor**laufzeit -1)
for j in range(1,laufzeit+1):    
    zinsen = kredit * zinssatz/100
    tilgung = annuitaet - zinsen
    verbleibend = kredit - tilgung
    print(f"Im Jahr {j} ist der Kredit {kredit}, die Zinsen {zinsen}, ihre Tilgung {tilgung}. Ihre Annuität ist {annuitaet} und der verbleibene Zins ist {verbleibend}")
    kredit = verbleibend