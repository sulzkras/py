# ПРИМЕР №1

# import pickle
#
#
# testlist = {"first": [1, 2], "secont": "str", "third": 123}
# with open("test.bin", "wb") as dFile:
# 	pickle.dump(testlist, dFile)
# newDict = {}
# with open("test.bin", "rb") as dFile:
# 	newDict = pickle.load(dFile)
# print(newDict)
# # OUT: {'first': [1, 2], 'secont': 'str', 'third': 123}
#
# class TestClass:
# 	num = 123
# 	strin = "str"
# 	spis = [1, 2, 3]
# 	slov = {"first": [1, 2], "secont": "str", "third": 123}
# 	cor = (22, 23)
#
# obj1 = TestClass()
# pikObj = pickle.dumps(obj1)
# print(f"Сериализация в байтовую строку \n{pikObj}")
# # OUT: Сериализация в байтовую строку
# # b'\x80\x04\x95\x1d\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tTestClass\x94\x93\x94)\x81\x94.'
#
# # obj1.spis = None
# # pikObj = pickle.load(pikObj)
# # print(pikObj.spis)
#
# class ProgressBar:
# 	def __init__(self):
# 		self.first = 0
# 		self.last = 100
# 		self.func = lambda x: x  = 1
#
# 	def __getstate__(self):
# 		attr = self.__dict__.copy()
# 		del attr["func"]
# 		return attr
#
# 	def __setstate__(self, state):
# 		self.__dict__ = state
# 		self.func = lambda x: x + 1
#
#
#
# obj2 = ProgressBar()
# pikObj2 = pickle.dumps(obj2)
# newObf = pickle.load(pikObj2)

# ПРИМЕР 2
#
# import json
# strok = "string"
# integ = 123456
# spis = {1,2,3}
#
# firstDict = {"first": strok, "second": integ, "third": spis}
# dumpJs = json.dump(firstDict)
# print(dumpJs)
#
# secondDict = json.load(dumpJs)
# print(secondDict)
#
# with open("upload.json", "w") as upJS:
# 	json.dump(secondDict, upJS)
#

# # ПРИМЕР 3
# import json
# class Test:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
#
# obj1 = Test(123, "asd")
# newObj = json.dumps(obj1, default = lambda x: x.__dict__)
# obj2 = json.loads(newObj)
# print(obj2)
# # OUT: {'a': 123, 'b': 'asd'}

# ПРИМЕР 3
import json
class Test:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
class TestEncoder(json.JSONEncoder):
	def default():
	
	
def to_json(obj):
	if isinstance(self, Test):
		result = self.__dict__
		result["className"] = self.__class__.__name__
		return result
		


obj1 = Test(123, "asd")
print(obj1.__dict__)
with open("test.json", "w", encoding = "utf-8") as fh:
	fh.write(json.dumps(obj1, default = to_json, ensure_ascii = False, indent = 4))
	
newObnj
obj2 = json.loads(newObj)
print(obj2)
# OUT: {'a': 123, 'b': 'asd'}