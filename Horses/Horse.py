from Horses import Horse

#Klasa opisująca konia
class Horse:
    name = ""
    favouriteNumber = 0
    age = 23

    def __init__(self):
        pass

    def __str__(self) -> str:
        return "Hi I'm " + self.name + " and I'm a unicorn"

    def Count(self):
        for x in range(self.favouriteNumber):
            print(x)

    def Drink(self):
        if self.age > 18:
            print("I'm drinking :)")
        else:
            #unieść wyjątek
            raise Exception("I'm not allowed to drink yet :(")

