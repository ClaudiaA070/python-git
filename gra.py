from html import entities
from re import X
from tkinter import Y




import random

choice = -1

while choice != 0:
    choice = input("Wybierz:\n[1] Kamień\n[2] Papier\n[3] Nożyce\n[0] Wyjście\n")
    choice = int(choice)

    computerChoice = random.randint (1,3)
    print("Komputer wybrał liczbę: " + str(computerChoice))

    if choice == 0:
        break
    elif choice == computerChoice:
        print("Remis! Prawie wygrałeś!")
        continue
    if choice == 1:
        if computerChoice == 2:
            print("Wygrał komputer")
        else:
            print("Wygrana!")
    elif choice == 2:
        if computerChoice == 3:
            print("Wygrał komputer")
        else:
            print("Wygrana!")
    elif choice == 3: 
        if computerChoice == 1:
            print("Niestety przegrałeś/łaś")
        else:
            print("Hurra! Wygrana!")