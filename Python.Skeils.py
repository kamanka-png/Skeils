a = float(input ("podaj pierwszą liczbę"))
b = float(input ("podaj drugą liczbę(bądź do której potęgi)"))
c = (input ("podaj działanie"))

if c =="dodawanie":
    wynik=a+b
    print(wynik)
elif c =="odejmowanie":
    wynik=(a-b)
    print(wynik)
elif c =="mnozenie":
    wynik=(a*b)
    print(wynik)
elif c =="dzielenie":
    if b==0:
        print("niedzielimy przez zero")
    else:
        wynik=(a/b)
        print(wynik)
elif c =="dzielenie modulo":
    if b==0:
        print("niedzielimy przez zero")
    else:
        wynik=(a%b)
elif c =="potęgowanie":
    wynik=(a**b)
    print(wynik)

    try:
        n = int(input ("podaj liczbę do której chcesz wypisać cyfry"))
    except ValueError:
        print("to nie jet liczba")

    def wypisz_liczby(n):
        if n < 1:
            return "nie mozna przyjąć tej liczby"
        elif n == 1:
            return 1
        else:
            wynik = 1 
        for i in range(1, n + 1):
            wynik += i
        return wynik
    print(wypisz_liczby(n))


try:
     n = int(input ("podaj ile chcesz kolejnych wartości ciągu Fibonacciego"))
except ValueError:
     print("To nie jest liczba")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))