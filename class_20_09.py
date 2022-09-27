# # ПРИМЕР №1
#
# class TestClass:
# 	def __init__(self, val = 1):
# 		self.prop1 = val
# 	def setProperty(self, val):
# 		self.prop2 = val
#
# object1 = TestClass()
# object2 = TestClass(2)
# object2.setProperty(3)
# object3 = TestClass(4)
# object3.prop3 = 5
#
# print(object1.__dict__)
# print(object2.__dict__)
# print(object3.__dict__)
#
# # Out: {'prop1': 1}
# # {'prop1': 2, 'prop2': 3}
# # {'prop1': 4, 'prop3': 5}

# # ПРИМЕР №2
#
# class TestClass:
# 	count = 0
# 	def __init__(self, val = 1):
# 		self.count = val
# 	def setProperty(self, val):
# 		self.prop2 = val
#
#
# object1 = TestClass()
# object2 = TestClass(2)
# object2.setProperty(3)
# object3 = TestClass(4)
# object3.prop3 = 5
#
# print(object1.__dict__, object1.count)
# print(object2.__dict__, object2.count)
# print(object3.__dict__, object3.count)
#
# # Out: {'_TestClass__prop1': 1}
# {'_TestClass__prop1': 2, '_TestClass__prop2': 3}
# {'_TestClass__prop1': 4, 'prop3': 5}


# ПРИМЕР №3

class TestClass:
	count = 0
	def __init__(self, val = 1):
		if val == 2:
			self.prop1 = 0
		else:
			self.prop3 = 2
	


object1 = TestClass()
try:
	print(object1.prop1)
except:
	print(object1.prop3)
	
#
print(object1.__dict__, object1.count)


# Out: 2
# {'prop3': 2} 0