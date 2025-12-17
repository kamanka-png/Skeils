n=int(input("Podaj liczbę całkowitą"))
x=int(input("podaj w jakim systemie chcesz to zrobić(2,3,8)"))
lista = []

if n<0:
    print("Liczba ma być dodatnia")
elif n==0:
        print("0")
else:
      while n>=1:
            reszta=n%x
            n=n//x
            lista.append(reszta)
print(lista)

