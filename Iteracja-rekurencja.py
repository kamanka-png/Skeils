#Stwórz program służący do obliczania silni za pomocą pętli iteracja
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

#Rekurencja Stwórz program obliczający silnię podanej liczby. 
n = int(input("Z jakiej liczby chcesz wywołać silnię"))

def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

print(silnia(n)) 


#trójkąt
try:
    a=int(input("podaj wysokosc trojkata"))
except ValueError:
    print("To nie jest licba")

if a < 1:
    print("nie mozna narysować trójkąta z liczb mniejszych od 1")
for i in range(a, 0, -1):
    print("*" * i)


#Stwórz program, który wypisze liczby od 1 do n rosnąco. 
try:
     n = int(input ("podaj liczbę"))
except ValueError:
     print("To nie jest liczba")

def wypisz_rekurencyjnie(n, aktualna_liczba=1):
  if aktualna_liczba <= n:
    print(aktualna_liczba)
    wypisz_rekurencyjnie(n, aktualna_liczba + 1)

wypisz_rekurencyjnie(n)


#Stwórz program sumujący wszystkie elementy listy. 
try:
   n= [int(x) for x in input("Podaj liczby, rozdzielone spacjami: ").split()]
except ValueError:
     print("Cyba coś pisałam na temat nie cyfr. To nie jest licba")

def lista(n):
    suma=0
    for i in n:
        suma+=i
    return suma
print(lista(n))