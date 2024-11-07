import matplotlib.pyplot as plt
import numpy as np
import csv as csv

while True:
    try:
        A = float(input("Podaj wartosc amplitudy oscylacji:"))
        if A < 0:
            raise ValueError()
        f = float(input("Podaj wartosc czestotliwosci:"))
        if f < 0:
            raise ValueError()
        y = float(input("Podaj wartosc wspolczynnika tlumienia:"))
        if y < 0:
            raise ValueError()
        a = float(input("Podaj amplitude szumu:"))
        if a < 0:
            raise ValueError()
        x = int(input("Podaj wektor czasu (dziedzine wykresu):"))
        if x < 0:
            raise ValueError()
        z = int(input("Podaj wartosc krokow wektora:"))
        if z < 0:
            raise ValueError()
    except ValueError:
        print("Wartosc musi byc dodatnia liczba")
        continue
    break

t = np.linspace(0, x, z)

E=np.exp(-y*t)
def sin (a,b,c,d,e):
    n= e * (np.random.rand(len(t)) - 0.5)
    # no=a * np.random.normal(size=t.size)-0.5
    return a*np.sin(2*np.pi*b*c)*d+n

real_sin=sin(A,f,t,E,a)

plt.scatter(t, real_sin)
plt.plot(t, real_sin)
plt.xlabel('Czas (t)')
plt.ylabel('Amplituda (A)')
plt.title('y=A*sin(2π*t*f)*e^(-y*t)+aN')
plt.show()

headline1 = t
data1 = t
Y = real_sin
headline2 = real_sin
data2 = real_sin

decision = input("Czy chcesz zapisać dane do pliku? Wpisz tak lub nie:")
if decision.lower() == 'tak':
    name = input("Podaj nazwę pliku bez rozszerzenia:")
    with open(f'./{name}.csv', mode='w') as file:
        writer=csv.writer(file)

        writer.writerow(['Czas (t)', 'Amplituda (A)'])
        for i in range(len(t)):
            writer.writerow([t[i], real_sin[i]])