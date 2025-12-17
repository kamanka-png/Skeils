n=int(input("Podaj liczbę całkowitą"))
def sito(n):
    if n < 2:
        return []
    sito = [True] * (n+1)

    sito[0], sito[1] = False

    for i in range(2, n+1):
        if sito[1]:
            j=i+i
            while j<= n:
                sito[j] = False
                j+=i
    return sito

sito=(n)

for i in range(len(sito)):
    if sito[i]:
        print(i)