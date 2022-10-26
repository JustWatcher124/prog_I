was = input("Alter, Geschlecht (M/W), trocknen (J/A), färben (J/N):")

age, sex, dry, color = was.split(",")
age = int(age)
price = 0

if sex in "Mm":
    if age <= 14:
        price += 10
    else:
        price += 14
else:
    if age <= 16:
        price += 12
    else:
        price += 20
if dry in "Jj":
    price += 5
if color in "Jj":
    price += 10

print("Ihre Frisur kostet Sie heute:", str(price) +"€.")
