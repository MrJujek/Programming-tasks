with open("./DANE/liczby.txt") as f:
    dane = f.read().split("\n")
print(dane)
max = 0
zapisana = 0
for liczba in dane:
    if liczba == '':
        continue

    odwrocona = int(liczba[::-1])

    absolutna = abs(int(liczba) - odwrocona)

    if absolutna > max:
        max = absolutna
        zapisana = liczba

print(zapisana, max)