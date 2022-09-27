class Stack:
    def __init__(self):
        self.__stackList = []
    def puch(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[- 1]
        del self.__stackList[-1]
        return val
    
class EditStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    def puch(self, val):
        self.__sum += val
        Stack.puch(self, val)
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    def getSumm(self):
        return self.__sum


obj1 = EditStack()
obj2 = EditStack()
obj3 = EditStack()

obj1.puch(4)
obj1.puch(4 )
obj1.puch(6)

print(obj3.getSumm()pop())




#
# class Machine:
#     """"описние класса"""
#     def __init__(self, whell, type, doors, color):
#         """конструктор класса"""
#         self.whell = whell
#         self.type = type
#         self.doors = doors
#         self.color = color
#     def drive(self):
#         """метов машина движется"""
#         return "It is driving"
#
#     def brake(self):
#         """метов машина останавливается"""
#         # return "It is braking"
#         return f"{self.color} {self.type} is braking"
#
# class WaterMachine(Machine):
#     def brake(self):
#         return f"{self.color} {self.type} is braking slooow"
#
# if __name__ == "__main__":
#     teh1 = Machine(4, "car", 5, "red")
#     teh2 = Machine(8, "truck", 2, "green")
#     teh3 = WaterMachine(0,"wCycle", 0, "blue")
#     print(teh1.color)
#     print(teh2.type)
#     print(teh1.brake())
#     print(teh2.drive())
#     print(teh3.drive())
#     print(teh3.color())
#     print(teh3.type())
#
    