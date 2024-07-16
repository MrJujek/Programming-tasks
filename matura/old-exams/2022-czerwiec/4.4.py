with open("./DANE/liczby.txt") as f:
    dane = f.read().split("\n")
# print(dane)
rozne = []
wystapienia1 = []
wystapienia2 = []
wystapienia3 = []
for liczba in dane:
    if liczba == '':
        continue

    if liczba not in rozne:
        rozne.append(liczba)

    if liczba not in wystapienia1 + wystapienia2 + wystapienia3:
        wystapienia1.append(liczba)
    elif liczba in wystapienia1:
        wystapienia2.append(liczba)
        wystapienia1.remove(liczba)
    elif liczba in wystapienia2:
        wystapienia3.append(liczba)
        wystapienia2.remove(liczba)

print(len(rozne))
print(len(wystapienia2))
print(len(wystapienia3))


