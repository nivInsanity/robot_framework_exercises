#Funkcja sprawdzająca, czy liczba jest pierwsza

def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

#Zmienna do przechowywania sumy
suma = 0

#Pętla for liczby od 2 do 100
for liczba in range(2,101):
    if czy_pierwsza(liczba):
        suma += liczba

#wyświetlenie wyniku
print("Suma liczb pierwszych do 100 wynosi:", suma)