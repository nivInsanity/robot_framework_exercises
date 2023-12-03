# Napisz program, który sprawdzi, czy podana liczba jest parzysta czy nie i wyświetli odpowiedni komunikat

def czy_parzysta(liczba):
    if liczba == 0:
        return None
    return liczba % 2 == 0


# Przykłąd użycia
liczba = int(input("Podaj liczbę do sprawdzenia: "))
wynik = czy_parzysta(liczba)

if wynik is None:
    print(f"Liczba {liczba} jest pomijana.")
elif wynik:
    print(f"Liczba {liczba} jest parzysta.")
else:
    print(f"Liczba {liczba} jest nieparzysta.")
