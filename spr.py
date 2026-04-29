historia = []

print("Witaj uzytkowniku!")
n = int(input("Podaj swoj stan konta (zl): "))
przychod = 0
wydatek = 0

while True:
    print("===MENU=== \n 1) Dodaj przychod \n 2) Dodaj wydatek \n 3) Sprawdz balans \n 4) Wyjdz i zapisz do pliku \n 5) Pokaz historie")
    n1 = int(input("Wybierz numer: "))

    if n1 == 1:
        przychod += n
        print("Przychod dodany:", przychod,"zl")
        historia.append("Przychod: " + str(przychod))
    elif n1 == 2:
        n = int(input("Dodaj wydatek: "))
        wydatek += n
        print("Wydatek dodany:", wydatek,"zl")
        historia.append("Wydatek: " + str(wydatek))
    elif n1 == 3:
        balans = przychod - wydatek
        print("Balans wynosi:", balans, "zl")
    elif n1 == 4:
        print("Koniec programu")
        with open("historia.txt", "w") as file:
            for element in historia:
                file.write(element + "\n")
        print("Zapisano do pliku txt")
        break
    elif n1 == 5:
        print(historia)
    else:
        print("Bledny wybor")











