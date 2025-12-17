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
