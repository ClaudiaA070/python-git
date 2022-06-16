import random

choice = -1


def GetInput():

    numberOne = input("Input first number: ")
    numberTwo = input("Input second number: ")
    numberOne = float(numberOne)
    numberTwo = float(numberTwo)

    return numberOne, numberOne


def Liczenie(numberOne,numberTwo):
    dodawanie = numberOne + numberTwo
    return dodawanie
    odejmowanie = numberOne - numberTwo
    return odejmowanie
    mnozenie = numberOne * numberTwo
    return mnozenie
    dzielenie = numberOne / numberTwo
    return dzielenie

def Dodawanie(numberOne, numberTwo):
    dodawanie = numberOne + numberTwo
    return dodawanie

def Odejmowanie(numberOne, numberTwo):
    odejmowanie = numberOne - numberTwo
    return odejmowanie




while choice != 0:
    choice = input("Wybierz działanie:\n[1] Dodawanie\n[2] Odejmowanie\n[3] Mnożenie\n[4] Dzielenie\n[0] Wyjście\n")
    choice = int(choice)


    if choice == 0:
        break
    a,b = GetInput()
    
    if choice == 1:
        result = Dodawanie(a, b)

    if choice == 2:
        result = Odejmowanie(a, b)

    if choice == 3:
        result = Mnozenie(a, b)

    if choice == 4:
        result = Dzielenie(a, b)

        print(result)



    """if choice == 1:
        #print(str(numberOne) + " + " + str(numberTwo) + " = " + str(numberOne + numberTwo))
    elif choice == 2:
        #print(str(numberOne) + " - " + str(numberTwo) + " = " + str(numberOne - numberTwo))
    elif choice == 3:
        #print(str(numberOne) + " * " + str(numberTwo) + " = " + str(numberOne * numberTwo))
    elif choice == 4:
        #print(str(numberOne) + " / " + str(numberTwo) + " = " + str(numberOne / numberTwo))

    """






"""
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
"""