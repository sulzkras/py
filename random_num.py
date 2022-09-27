import random
magic_num = random.randint(10,30)
user_num=0
while magic_num != user_num:
    user_num = int(input("Введите число от 1 до 500: "))
    if user_num > magic_num:
        print("Число должно быть МЕНЬШЕ, попробуйте снова...")
    elif user_num < magic_num:
        print("Число должно быть БОЛЬШЕ, попробуйте снова...")
    else:
        print("Поздравляю, Вы угадали число!", user_num)
