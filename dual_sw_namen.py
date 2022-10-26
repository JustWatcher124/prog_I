vor = input("Vornamen:")
nac = input("Nachnamen:")
geb = input("Geburtsstadt:")
par = input("Partnerunternehmen:")

dual = vor[:3].lower() + nac[:2].lower()
dual = dual[0].upper() + dual[1:]

mit = nac[:3].lower() + vor[:2].lower()
mit = mit[0].upper() + mit[1:]

nacn = geb[:2].lower() + par[:3].lower()
nacn = nacn[0].upper() + nacn[1:]

print("Hallo,", dual,mit,nacn)