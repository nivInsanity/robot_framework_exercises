#Zbuduj funkcję kalkulatora, ktory przyjmuje dwie liczby matematyczne i operator matematyczny (+,_,*,:) i zwraca wynik

#Pobieranie pierwszej liczby od użytkownika
liczba1= float(input("Podaj pierwszą liczbę: "))

#Pobieranie drugiej liczby od użytkownika
liczba2 = float(input("Podaj drugą liczbę: "))

#Pytanie użytkowanika o rodzaj operacji
operacja = input("Wybierz operację (wpisz '+', '-', '/' lub '*'): ").lower()

#Wykonanie operacji dodawania, odemowania, dzielenia lub mnożenia
if operacja == "+":
    wynik = liczba1 + liczba2
    print(f"Wynik dodawania: {wynik}")
elif operacja == "-":
    wynik = liczba1 - liczba2
    print(f"Wynik odejmowania: {wynik}")
elif operacja == "/":
    wynik = liczba1 / liczba2
    print(f"Wynik dzielenia: {wynik}")
elif operacja == "*":
    wynik = liczba1 * liczba2
    print(f"Wynik mnożenia: {wynik}")
else:
    print("Niepoprawny wybór operacji")