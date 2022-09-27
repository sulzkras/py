# import random
# myList = [random.randint(7,20) for h in range(20)]
# print(myList)
# myList1 = myList[0:12]
# print("Две трети списка: ", myList1)
# if sum(myList1) / 12 >= 0:
# 	myList1.sort()
# 	print("Две трети списка по возрастанию:", myList1)
# 	myList3 = myList1[::-1]
# 	print("Две трети списка в обратно порядке:", myList3)
# myList4 = myList[12:]
# print("Остаток списка: ", myList4)
# myList5 = myList4[::-1]
# print("Остаток списка в обратном порядке: ", myList5)

import random
myList = [random.randint(1,12) for h in range(10)]
print("Оценки студента Васи: ", myList)
a = int(input("Введите номер порядковый номер отметки: "))
b = int(input("Введите новую отметку: "))
myList1 = myList.insert(a, b)
print(myList1)
