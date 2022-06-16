from Horses.Horse import Horse
from Horses.Unicorn import Unicorn

myHorsesList = []


myHorse = Horse()
myHorse.name = "Applejack"
myHorse.favouriteNumber = 5

myHorse2 = Horse()
myHorse2.name = "Fluttershy"
myHorse2.favouriteNumber = 295

myUnicorn = Unicorn()
myUnicorn.name = "Twilight Sparkle"
myUnicorn.cornColor = "Pink"
myUnicorn.favouriteNumber = 8

myUnicorn2= Unicorn()
myUnicorn2.name = "Rainbow Dash"
myUnicorn2.cornColor = "Red-Yellow-Green-Blue"
myUnicorn2.favouriteNumber = 40000

myHorsesList.append(myHorse)
myHorsesList.append(myUnicorn)
myHorsesList.append(myHorse2)
myHorsesList.append(myUnicorn2)

                    #gdzie  
unicorns = filter(lambda h: h.favouriteNumber < 10, myHorsesList)
for unicorn in unicorns:
    print(unicorn)

# obsługa wyjątków
for horse in myHorsesList:
    try:
        horse.Drink()
    except:
        print(horse.name + " cannot drink yet...")


for horse in myHorsesList:
    print(horse)

    if type(horse) is Unicorn:
        print(horse.cornColor)

