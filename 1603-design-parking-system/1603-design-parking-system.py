class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.pslots = [big,medium,small]
        

    def addCar(self, carType: int) -> bool:
        if(self.pslots[carType-1]==0):
            return False
        else:
            self.pslots[carType-1]-=1
            return True