def najwieksza_liczba_wykladow(n, wyklady):
    # Sortujemy wykłady według czasu zakończenia
    wyklady.sort(key=lambda x: x[1])

    # Inicjalizujemy zmienne
    wyklady_wybrane = []
    ostatni_koniec = 0

    # Wybieramy wykłady
    for i in range(n):
        if wyklady[i][0] > ostatni_koniec:
            wyklady_wybrane.append((i+1, 0))
            ostatni_koniec = wyklady[i][1]

    # Wypisujemy wynik
    print(len(wyklady_wybrane))
    for wyklad in wyklady_wybrane:
        print(wyklad[0], wyklad[1])

# Wczytywanie danych
n = int(input())
wyklady = [list(map(int, input().split())) for _ in range(n)]

# Wywołanie funkcji
najwieksza_liczba_wykladow(n, wyklady)
