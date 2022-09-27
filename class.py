# strok = "strok"
# print(dir(strok))

class Machine:
    """"описние класса"""
    def __init__(self, whell, type, doors, color):
        """конструктор класса"""
        self.whell = whell
        self.type = type
        self.doors = doors
        self.color = color
    def drive(self):
        """метод машина движется"""
        return "It is driving"
        
    def brake(self):
        """метод машина останавливается"""
        # return "It is braking"
        return f"{self.color} {self.type} is braking"
    
class WaterMachine(Machine):
    def brake(self):
        return f"{self.color} {self.type} is braking slooow"
    
if __name__ == "__main__":
    teh1 = Machine(4, "car", 5, "red")
    teh2 = Machine(8, "truck", 2, "green")
    teh3 = WaterMachine(0, "wCycle", 0, "blue")
    print(teh1.color)
    print(teh2.type)
    print(teh1.brake())
    print(teh2.drive())
    # print(teh3.drive())
    # print(teh3.color())
    # print(teh3.type())
    
    