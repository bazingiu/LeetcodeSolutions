from collections import defaultdict

prova  = defaultdict(int)
prova["cane"] += 1
prova[1] = 20

print(prova.keys())
print(prova.values())
print(prova.items())