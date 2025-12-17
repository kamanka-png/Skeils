#sito_etatostensa
n=int(input("Podaj liczbę całkowitą"))
def sitoEratostenesa(n):
    if n < 2:
        return []
    sito = [True] * (n+1)

    sito[0], sito[1] = False, False

    for i in range(2, n+1):
        if sito[1]:
            j=i+i
            while j<= n:
                sito[j] = False
                j+=i
    return sito

sitoWynik=sitoEratostenesa(n)

for i in range(len(sitoWynik)):
    if sitoWynik[i]:
        print(i)

#Generowanie wyrazów w ciągi Fibonacciego iteracyjnie
def fibonacci_iteracyjnie(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2]) 
    return fib[:n]

n=int(input("Podaj liczbę całkowitą"))
print(fibonacci_iteracyjnie(n))

#Generowanie wyrazów w ciągi Fibonacciego rekurencyjnie
def fibonacci_rekurencyjnie(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rekurencyjnie(n-1) + fibonacci_rekurencyjnie(n-2)

n=int(input("Podaj liczbę całkowitą"))
for i in range(n):
    print(fibonacci_rekurencyjnie(i))


#Obliczanie silni iteracyjnie
try:
    n = int(input ("podaj liczbę"))
except ValueError:
    print("To nie jest liczba")

def oblicz_silnie(n):
    if n < 0:
        return "Silnia nie jest zdefiniowana dla liczb ujemnych."
    elif n == 0:
        return 1
    else:
        wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik
print(oblicz_silnie(n))

#Obliczanie silni rekuracynie
n = int(input("Z jakiej liczby chcesz wywołać silnię"))

def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

print(silnia(n)) 

#Rozkład na czynniki pierwsze
x=int(input("Podaj liczbę całkowitą"))
    
def czynniki_pierwsze(liczba):
    czynniki= []
    dzielnik= 2
    while liczba !=1:
        while liczba % dzielnik == 0:
            czynniki.append(dzielnik)
            liczba //= dzielnik
        dzielnik += 1 
    return czynniki
print(czynniki_pierwsze(x))

#Zamiana liczby dziesiętnej na binarną
def dziesietna_na_binarna_manualnie(n):
    if n == 0:
        return "0"
    binarny = ""
    while n > 0:
        reszta = n % 2
        binarny = str(reszta) + binarny
        n //= 2
    return binarny

liczba = int(input("Podaj liczbę całkowitą"))
print(dziesietna_na_binarna_manualnie(liczba))

#Zamiana liczby binarnej na dziesiętną
def binarna_na_dziesietna_rekurencyjnie(b):
    if len(b) == 0:
        return 0
    else:
        return int(b[0]) * (2 ** (len(b) - 1)) + binarna_na_dziesietna_rekurencyjnie(b[1:])

liczba_binarna =int(input("Podaj liczbę w forme binarnej"))
print(binarna_na_dziesietna_rekurencyjnie(liczba_binarna))


#Szukanie najmniejszego lub największego elementu w liście
with open("liczby.txt", "r") as file:
    content = file.readlines()

min_number = float('inf')
max_number = float('-inf')
min_line = -1
max_line = -1

for index, line in enumerate(content):
     number = int(line.strip())
     if number < min_number:
            min_number = number
            min_line = index + 1 
     if number > max_number:
            max_number = number
            max_line = index + 1

print(f"Najmniejsza liczba jest w wierszu: {min_line}")
print(f"Największa liczba jest w wierszu: {max_line}")

#Porównywanie tekstów
n = input ("podaj wzorzec piewszy")
m = input ("podaj wzorzec drugi")
if n==m:
    print("true")
else:
    print("false")

#Odwracanie kolejności liter w wyrazie
def odwroc_wyraz_iteracyjnie(wyraz):
    odwrocony_wyraz = ""
    for litera in wyraz:
        odwrocony_wyraz = litera + odwrocony_wyraz
    return odwrocony_wyraz

wyraz = int("Podaj słowo do odwrócenia")
print(odwroc_wyraz_iteracyjnie(wyraz))

#Zliczanie wystąpień podanego znaku w tekście
def zlicz_wystapienia(tekst, znak):
    return tekst.count(znak)

tekst = int("Podaj tekst w jakim chcesz zliczyć wystąpienia")
znak = int(input("Jaki chcesz znak zliczyć"))
print(zlicz_wystapienia(tekst, znak))

#Szukanie wzorca w tekście
tekst = int("Wczytaj tekst we którym chcesz znaleść wzorzec")
wzorzec = int("Podaj jaki chcesz wzorzec znaleść")

