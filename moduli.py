# СУММА ЧИСЕЛ
# def sum_num(a, b):
# 	total = 0
# 	for i in range(a, b+1):
# 		total += i
# 	return total
# print(sum_num(2, 3))

# ПРОВЕРКА ПРОСТОГО ЧИСЛА
# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2 + 1):
# 	if a % i == 0:
# 		k = k + 1
# if (k <= 0):
# 	print("Число", a, "простое")
# else:
# 	print("Число", a, "не является простым")
	

# ПРОВЕРКА СЧАСТЛИВОГО ЧИСЛА
a = int(input('Введите номер билета: '))
sum_left = 0
sum_right = 0
for i in range(6):
    if i < 3:
        sum_right += a // 10**i % 10
    else:
        sum_left  += a // 10**i % 10
if sum_left == sum_right:
    print('lucky')
else:
    print('unlucky')

