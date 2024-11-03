def nwd(a, b):
    dzielnik = odp = 2
    while dzielnik <= a:
        if a % dzielnik == 0 == b % dzielnik:
            odp = dzielnik
        dzielnik += 1
    return odp

print(nwd(75, 100))