sent = input("Write an english sentence: ").lower()
d = {
    "ee": "ie", "oo" : "u", "sh": "sch", "oy": "eu",
    "th": "s", "ai": "äh", "ae": "ä", "ce" : "ße",
    "e": "i", "a": "ä", "z": "s", "u":"a"
}
for i in d.keys():

    sent = sent.replace(i, d[i])

print(sent)

roman = input("eine römische zahl eingeben:")

d = {
    "CM":"DCCCC", "M":"DD", "CD":"CCCC", "D":"CCCCC",
    "XC":"LXXXX", "C":"LL", "XL":"XXXX", "L":"XXXXX",
    "IX":"VIIII", "X":"VV", "IV":"IIII", "V":"IIIII"
}

for i in d.keys():
    roman = roman.replace(i,d[i])

print(len(roman))