# Klasa opisująca kalkulator
class Calculator:
    memory = 0

    def _init_(self):
        self.memory = 0

# Operacje matematyczne
def Add(self, number1, number2):
    return number1 + number2

def Subtract(self, number1, number2):
    return number1 - number2


# Zarządzanie pamięcią
def MemPlus(self, number):
    self.memory += number
    
def MemMinus(self, number):
    self.memory -= number

def MemCheck(self):
    return self.memory

    # KONIEC KLASY


naszKalkulator = Calculator()
result = naszKalkulator.Add(4, 6)
naszKalkulator.MemPlus(result)

print(naszKalkulator.MemCheck())

result = naszKalkulator.Subtract(4, 6)
naszKalkulator.MemMinus(result)

print(naszKalkulator.MemCheck())