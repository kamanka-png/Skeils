try:
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
except ZeroDivisionError:
    print("Nie mona dzielić przez zero")
except ValueError:
    print("To nie jest liczba")