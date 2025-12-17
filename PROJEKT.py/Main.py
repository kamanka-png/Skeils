import powitanie
import wiek

def main():
    while True:
        print("=== BIBLIOTEKA PROGRAMÓW W PYTHONIE ===")
        print("1 - Powitanie")
        print("2 - Wiek")
        print("0 - Wyjście")

        try: 
            wybor = int(input("Wybierz opcję: "))
        except ValueError:
            print ("Podaj poprawny numer!")
            continue

        if wubor == 1:
            powitanie .powitanie()
        elif wybor == 2:
            wiek.ileLat()
        elif wubor == 0:
            print("Koniec programu. Do zobaczenia!")
            break
        else:
            print("Nie ma takiej opcji!")

if __name__ == "_main__":
    main()