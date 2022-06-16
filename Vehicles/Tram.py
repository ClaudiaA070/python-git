from Vehicles.Vehicle import VehicleClass

class Tram (VehicleClass):

    def __init__(self):
        super().__init__()
        
    def PantographUp(self):
        self.pantographUp = True
        print("Pulling pantograph up...")

    def PantographUp(self):
        self.pantographUp = False
        print("Putting pantograph down...")
