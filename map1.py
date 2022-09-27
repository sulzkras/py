
list1 = [x for x in range(5)]
list2 = list(map(lambda  x: 2 ** x, list1))
print(list2)

from random import randint

data = [randint(-10, 10) for x in range]