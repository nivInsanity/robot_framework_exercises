# Średnia arytmetyczna

print("*** Średnia arytmetyczna ***")
a = 5
b = 4
c = 6
print("Średnia wynosi:", (a+b+c)/3)

# Napisz program, który obliczy średnią arytmetyczną z trzech liczb podanych przez użytkownika i
# wyświetli wynik na konsoli.

print("*** Średnia arytmetyczna - oblicz ***")
a = input("Podaj pierwszą liczbę?")
a = int(a)
b = input("Podaj drugą liczbę?")
b = int(b)
c = input("Podaj trzecią liczbę?")
c = int(c)
srednia = (a+b+c)/3
print('Średnia arytmetyczna z podanych liczb to:', srednia)

####################################################################################################
# Zadanie 2: Konwersja Stopni Celsiusza na Fahrenheita
# Poproś użytkownika o podanie temperatury w stopniach Celsjusza, a następnie przelicz ją na stopnie
# Fahrenheita. Wykorzystaj wzór: F = (C * 9/5) + 32, gdzie F to temperatura w Fahrenheita, a C to
# temperatura w Celsjusza.

print("*** Konwersja Stopni Celsiusza na Fahrenheita ***")
# F = (C * 9/5) + 32
C = input("Podaj temperaturę w stopniach celcjusza?")
C = int(C)
F = (C * 9/5) + 32
print(C, "stopnie Celcjusza to", F, "stopni Farenheita")

# Napisz program, który pozwoli użytkownikowi wprowadzić swoją masę (w kilogramach) i wzrost (w
# metrach), a następnie obliczy jego wskaźnik masy ciała (BMI).
# Wykorzystaj wzór: BMI = masa / (wzrost * wzrost). Następnie wyświetl kategorię BMI (np.
# "niedowaga", "waga prawidłowa", "nadwaga", "otyłość") na podstawie obliczonego wyniku.

print("*** Kalkulator BMI ***")
waga = input("Podaj ile ważysz (kg)?")
wzrost = input('podaj ile masz wzrostu (cm)?')

waga = int(waga)
wzrost = int(wzrost)

BMI = (waga / (wzrost*wzrost))*10000

print('Twoje BMI to:', BMI)

if BMI <= 18.50:
    print("niedowaga 🤔")
elif 18.50 < BMI <= 25:
    print("prawidłowa masa ciała 😎")
elif 25 < BMI <= 30:
    print("nadwaga 😪")
elif 30 < BMI:
    print("otyłość 😭")
