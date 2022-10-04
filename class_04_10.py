# ПРИМЕР №1

# class Node:
#
# 	def __init__(self, data):
# 		self.data = data
# 		self.nextNode = None
# 		self.pre = None
#
#
# obj1 = Node("str")
# obj2 = Node(1)
# obj3 = Node(2)
#
# obj1.nextNode = obj2
# obj2.nextNode = obj3

# ПРИМЕР №2

class Elem:
	# узлы связного списка
	def __init__(self, item):
		self.nextItem = item
		self.nextItem = None
		
		
class Node:
	
	 # связный список
	def __init__(self):
		self.head = None
	
	def append(self, newItem):
		newItem = Elem(newItem)
		if self.head is None:
			self.head = newItem
			return
		lastElem = self.head
		while lastElem.nextItem:
			lastElem = lastElem.nextItem
		lastElem.nextItem = newItem
		
	
	def __contains__(self, item):
		lastElem = self.head
		while lastElem:
			if item == lastElem.item:
				return True
			else:
				lastElem = lastElem.nextItem
		return False
	
	def __getitem__(self, itemIdex):
		lastElem - self.head
		elemIndex = 0
		while elemIndex <=itemIdex:
			if elemIndex == itemIdex
				return lastElem.item
			elemIndex += 1
		 
obj1 = Node()
obj1.append(1)
obj1.append(2)
obj1.append(3)
print(obj1.__contains__(2))
print(obj1 )

	
