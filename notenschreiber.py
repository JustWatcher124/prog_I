s = input("Eine Notenreihenfolge ohne Leerzeichen z.B. ABEF: ")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
notes = {
    "A": "- - -o- -",
    "B": "- - o - -",
    "C": "- -o- - -",
    "D": "- o - - -",
    "E": "-o- - - -",
    "F": "- - - -o-",
    "G": "- - - o -"
    }

l = ["" for i in range(9)]

for i in s:
    for b in range(9):
        l[b] += notes[i][b]

for i in l:
    print(i)
