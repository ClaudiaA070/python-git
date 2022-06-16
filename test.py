from html import entities
from re import X
from tkinter import Y


print(" - - - - - - - POCZĄTEK PROGRAMU - - - - - - - - ")

"""
Komentarze
wielolinijkowe

"""

#zmienne



ageLimit = 18


#dane
firstName = input("What is your name?")
lastName = input("What is your last name?")
age = input("How old are you?")
age = int(age)


#welcome = "Hi! \nMy name is " + firstName + " " + lastName + "."
#print(welcome)

# sprawdzanie pelnoletnosci

isUnderage = age < ageLimit #typ: bool
print(type(isUnderage))
if not isUnderage and not firstName.endswith("a"):
   # print("I'm over 18 yeras old.")
   print("Jestem pełnoletni")
elif not isUnderage:
    print("Jestem pełnoletnia")
else:
    print("I'm underage.")

#5! = 1 * 2 * 3 * 4 * 5  = 4! * 5
# 4! = 1 * 2* 3 * 4      = 3! * 4   itd..

def Factorial (number):
    if number ==1:
        return 1

    return Factorial(number - 1)* number

# policzenie silni z podanego wieku
ageFactorial = Factorial(age)
print(str(age) + "! = " + str(ageFactorial))