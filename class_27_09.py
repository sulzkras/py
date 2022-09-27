# #  ПРИМЕР №1
#
# class TestClass:
# 	def __init__(self, a, lists):
# 		self.a = a
# 		self.lists = list(lists)
# 	def __getitem__(self, item):
# 		return self.lists[item]
# 	def __setitem__(self, key, value):
# 		if not isinstance(key, int):
# 			raise TypeError('Индекс должен быть целым число')
# 		if key >= len(self.lists):
# 			last = key + 1 - len(self.lists)
# 			self.lists.extend(([None]*last))
# 		self.lists[key] = value
#
# 	def __delitem__(self, key):
# 		del self.lists[key]
#
# obj1 = TestClass("Объект", [1,2,3,4,5,6])
# print(obj1.lists[0])
# print(obj1[2])
# obj1[10] = 9
#
# print(obj1.lists)
#

#  ПРИМЕР №2

class Teacher:
	def learnStudent(self, *predm):
		
		"""Предметы"""
		self.predm = predm
		
		
		""""Выдача знаний"""
	def drive(self):
		return "Learning knowledge"

class Student:
	def __getitem__(self, item):
		return self.knowledge
	def __setitem__(self, item):
		return self.knowledge

class Knowledge:
	def __init__(self, history, geograthy, maths):
		self.history = history
		self.geograthy = geograthy
		self.maths = maths


obj1 = Teacher()
print("Объем знаний выданный учителем", obj1.)


