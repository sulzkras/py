import random
myList = [random.randint(7,10) for h in range(10)]
# obrasezList = myList.sort()
# print("Идеальный список", obrasezList)
print("Список оладий:", myList)
# while
srez = int(input("Введите порядковый номер оладьи в стопке: ", ))
myList_up = myList[srez:]
print("Остается в верхней стопке ",myList_up)
myList_down = myList[:srez]
print("Остается в нижней стопке ",myList_down)
myList_rev = myList_up[::-1]
print("Перевернутая стопка", myList_rev)
newList = myList_rev + myList_down
print("Получилась такая стопка", newList)
# print(myList)

