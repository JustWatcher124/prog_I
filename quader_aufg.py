breite = float(input("Breite (in cm):"))
laenge = float(input("Länge (in cm):"))
hoehe = float(input("Höhe (in cm):"))

vol = breite*laenge*hoehe
print("(in cm³):", vol)

print(f"(in l): {vol/1000:.2f}")

flaech = (breite*laenge + breite*hoehe + laenge*hoehe)*2
print("flrache des quaders in cm²", flaech)