with open("./DANE/liczby.txt") as f:
    dane = f.read().split("\n")
print(dane)

def sito(n):
    liczby = [True for _ in range(n)]
    pierwsze = []

    for i in range(len(liczby)):
        if i <= 1:
            liczby[i] = False
        else:
            if liczby[i] == True:
                pierwsze.append(i)
                for j in range(i, len(liczby), i):
                    liczby[j] = False

    return pierwsze
pierwsze = sito(100000)
print(pierwsze)
for liczba in dane:
    if liczba == '':
        continue

    odwrocona = int(liczba[::-1])

    if int(liczba) in pierwsze and odwrocona in pierwsze:
        print(liczba)

