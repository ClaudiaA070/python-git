from html import entities
from re import X
from tkinter import Y


print(" - - - - - - - POCZĄTEK PROGRAMU - - - - - - - - ")

"""
Komentarze
wielolinijkowe

"""
# komentarz linijkowy

#zmienne
#ageLimit = 18


numberOne = input("Podaj pierwszą liczbę")
numberTwo = input("Podaj drugą liczbę")

numberOne = int(numberOne)
numberTwo = int(numberTwo)

dodawanie = numberOne + numberTwo
odejmowanie = numberOne - numberTwo
mnożenie = numberOne * numberTwo
dzielenie = numberOne / numberTwo

wynik = input("Jaką operację chcesz wykonać (dodawanie, odejmowanie, mnożenie, dzielenie)?")

print("wynik")



if wynik == "dodawanie":
    print(dodawanie)
elif wynik == "odejmowanie":
    print(odejmowanie)
elif wynik == "mnożenie":
    print(mnożenie)
else:
    print(dzielenie)
    

    numberOne = input("Input first number: ")
    numberTwo = input("Input second number: ")
    numberOne = float(numberOne)
    numberTwo = float(numberTwo)

    if choice == 1:
        print(str(numberOne) + " + " + str(numberTwo) + " = " + str(numberOne + numberTwo))
    elif choice == 2:
        print(str(numberOne) + " - " + str(numberTwo) + " = " + str(numberOne - numberTwo))
    elif choice == 3:
        print(str(numberOne) + " * " + str(numberTwo) + " = " + str(numberOne * numberTwo))
    elif choice == 4:
        print(str(numberOne) + " / " + str(numberTwo) + " = " + str(numberOne / numberTwo))

    numberOne, numberTwo = GetInput()

fruits = ["apple", "banana", "pear", "orange", "strawberry"]
for fruit in fruits:
    if fruit == "banana":
        print("YELLOW")
        continue

    print(fruit)
else:
    print("All the fruits!")

for i in range(7):
    index = random.randint(0, len(fruits) - 1)
    print(fruits[index])

for i in range(5):
    index = random.randing(0,3)
    print(fruits[index])


