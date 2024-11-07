class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko}.')

    def zmien_nazwisko(self, nowe_nazwisko):
        self.nazwisko = nowe_nazwisko

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

osoba = Osoba('Jan', 'Kowalski')
osoba.przedstaw_sie()
osoba.zmien_nazwisko('Nowak')
osoba.przedstaw_sie()
osoba.imie = 'Adam'
osoba.przedstaw_sie()
print(osoba)
