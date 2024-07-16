with open("./DANE/liczby.txt") as f:
    dane = f.read().split("\n")
print(dane)

for liczba in dane:
    if liczba == '':
        continue
    odwrocone = str(liczba)[::-1]
    if int(odwrocone) % 17 == 0:
        print(odwrocone)

