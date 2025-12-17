# if 5>3:
#     print("Prawda")

# #a=10/0

# def srednia(a, b):
#     return a+b/2
# print(srednia(4,6))

# print(0.1+0.2)

try:
    x=int(input("Podaj liczbe:"))
    print(10/x)
except ZeroDivisionError:
    print("Nie mona dzielić przez zero")
except ValueError:
    print("To nie jest liczba")


lista=[1,2,3]
try:
    print(lista[5])
except ImportError:
    print("Nie ma takiego elememntu w liście")