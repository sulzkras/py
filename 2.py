while True:
	a = input("Введите число А: ")
	oper = input("Введите операцию: ")
	b = input("Введите число B: ")
	if a.isnumeric() and b.isnumeric():
		break
	else:
		print("Вы должны ввести число!: ")
		continue
result = 0

while True:
	if (oper == "+") or (oper == "-") or (oper == "*") or (oper == "/"):
		break
	else:
		print("Вы должны ввести операцию!:...")
		continue
if oper == "+":
	result = int(a) + int(b)
	# print(result)
elif oper == "-":
	result = int(a) - int(b)
	# print(result)
elif oper == "*":
	result = int(a) * int(b)
	# print(result)
elif oper == "/":
	result = int(a) / int(b)
	# print(result)
print(f"A{oper}B={result}")
