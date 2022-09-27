import string
# userLogin = input("Введите логин: ")
import re
while True:
	userPassword = input('Придумайте пароль: ')
	pass_len = len(userPassword)
	pass_low = sum(map(str.islower, userPassword))
	pass_up = sum(map(str.isupper, userPassword))
	pass_dig = sum(map(str.isdigit, userPassword))
	if (pass_len < 8) or (pass_up < 1) or (pass_dig < 3):
		print('Пароль ненадёжный. Попробуйте ещё раз.')
	else:
		print('Это надёжный пароль!')
		break
while True:
	userLogin = input('Придумайте логин: ')
	pass_len = len(userLogin)
	pass_low = sum(map(str.islower, userLogin))
	pass_up = sum(map(str.isupper, userLogin))
	pass_dig = sum(map(str.isdigit, userLogin))
	if (pass_len < 8) or (pass_up < 1) or (pass_dig < 3):
		print('Этот логин ненадёжный. Попробуйте ещё раз.')
	else:
		print('Логин введен верно!')
		break

while True:
	userEmail = input('Введите адрес электронной почты: ')
	match = re.search(r'\@', userEmail)
		print('YES' if match else 'NO')
	# 	print('Логин ненадёжный. Попробуйте ещё раз.')
	# else:
	# 	print('Вы зареганы!')
	# 	break


