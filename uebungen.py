matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
x = [ [ row[i] for row in matrix ] for i in range( max(len(r) for r in matrix))]

dnf = [i for i in range(101) if i % 3 == 0 if i % 5 != 0]
print("Liste 1:", dnf)


ndbd = [i for i in range(101) if i % 3 != 0 if "3" in str(i)]
print("Liste 2:", ndbd)

sentence = " the quick brown fox jumps over the lazy dog "
print("Liste 3:",[len(wl) for wl in sentence.split() if wl != "the"])

print("Liste 2:","".join([i for i in sentence if i not in "aeiou"]))


for i in range(1,10001):
    if sum([b for b in range(1,i) if i % b == 0]) == i:
        print(i)
