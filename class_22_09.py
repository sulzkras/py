#  ПРИМЕР №1

# class Star:
# 	def __init__(self, name, galaxy):
# 		self.name = name
# 		self.galaxy = galaxy
#
# 	def __str__(self):
# 		return self.name + ' в галактике ' + self.galaxy
#
# sun = Star("Ригель", 'Млечный путь')
# print(sun.__str__())

#  ПРИМЕР №2

# class Machine:
# 	pass
# class EarthMachine(Machine):
# 	pass
# class Track(EarthMachine):
#
# for class1 in [Machine, EarthMachine, Track]:
# 	for class2 in [Machine, EarthMachine, Machine]:
# 		print(class1.__name__, issubclass(class1, class2), class2.__name__, sep = '\t')
# myMachine = Machine()
# myEarthMachine = EarthMachine()
# myTrack = Track()
# for obj in [myMachine, myEarthMachine, myTrack]:
# 	for class2 in [Machine, EarthMachine, Track]:
# 		print((issubclass(obj, class2), class2.__name__, sep ="\t"))

# #  ПРИМЕР №3
#
# class Super:
# 	def __init__(self, name):
# 		self.name = name
# 	def __str__(self):
# 		return "Меня зовут " + self.name
#
# 	# supParam = 1
# class Sub(Super):
# 	def __init__(self, name):
# 		Super.__init__(self, name)
# 		# supper().__init__(name)
# 		# pass
# 	subParam = 2
# obj = Sub('Антон')
# print(obj)

# # ПРИМЕР №4
#
# class Root:
# 	def __init__(self):
# 		self.rootParam = 22
#
# class Sub(Root):
# 	def __init__(self):
# 		super().__init__()
# 		self.subParam == 33
#
# obj = Sub()
# print(obj.rootParam)
# print(obj.subtParam)

# ПРИМЕР №6

# class RootA:
# 	param = 10
# 	def
# 		fun(self):
# 		return 11
#
#
# class RootB:
# 	param = 20
# 	def
# 		fun(self):
# 		return 21
# class RootC:

# # ПРИМЕР №6
#
# class One:
# 	def doit(self):
# 		print('Метод класса 1')
# 	def doinany(self):
# 		self.doit()
#
# class Two(One):
# 	def doit(self):
# 		print('Метод класса 2')
#
# obj1 = One()
# obj2 = Two()
# obj1.doinany()
# obj2.doinany()
# 	def doinany(self):
# 		self.doit()
#
# ПРИМЕР №7

# import time
#
# class Machine:
# 	def changeDirection(self, onj):
# 		pass
# 	def turn(self):
# 		pass
#
# 	def turn(self):
# 		self.controlDirection(True)
# 		time.sleep(1)
# 		self.controlDirection(False)
#
# class Track:
# 	def controlTrack(self, stop):
# 		pass
# 	def turn(self):
# 		self.controlTrack(True)
# 		time.sleep(1)
# 		self.controlTrack(False)
#
# class Wheel:
# 	controlWheel(self, stop):
# 		pass
# 	def turn(self):
# 		self.controlWheel(True)
# 		time.sleep(1)
# # 		self.controlWheel(False)
# import time
#
# # ПРИМЕР №8
# class Machine:
# 	def __init__(self, controller):
# 		self.controller = controller
# 	def turn(self):
# 		self.controller.changeDirection(self, True)
# 		time.sleep()
# 		self.controller.changeDirection(self, False)
#
# class Track:
# 	def changeDirection(self, on):
# 		print('track', on)
#
# class Wheel:
# 	def changeDirection(self, on):
# 		print('wheel', on)
#
# myWheeled = Machine(Wheel())
# myTracked = Machine(Track())
# myWheeled.turn()
# myWheeled.turn()
#

# ПРИМЕР №9
# class Class1:
# 	pass
#
# class B(A):
# 	pass
#
# class C(A):
# 	pass
#
# class A:
# 	pass

# # ПРИМЕР
#
# def rec(n):
# 	try:
# 		n = 1 / n
# 	except ZeroDivisionError:
# 		print('ZeroDivisionError')
# 		return None
# 	else:
# 		print('Nothin to do')
# 		return n
# 	finally:
# 		print('Some code')
# print(rec(2))
# print(rec(0))

# # ПРИМЕР №6
#
# def printExeption(thisClass, attach = 0):
# 	if attach > 1:
# 		print('|' * (attach - 1), end = "")
# 	if attach > 0:
# 		print('+---', end = "")
# 	print((thisClass.__name__))
# 	for sub in thisClass.__subclasses__():
# 		printExeption(sub, attach + 1)
# printExeption(BaseException)

# ПРИМЕР №10

class MyZerroDivisionError(ZerroDivisionError)

