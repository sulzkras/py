import random
magic_num = random.randint(0,500)
user_num=-1
while magic_num != user_num:
    user_num = int(input("Введите число от 1 до 500: "))
    if user_num > magic_num:
        print("Число должно быть меньше, попробуйте снова...")
    elif user_num < magic_num:
        print("Число должно быть больше, попробуйте снова...")
    else:
        print("Поздравляю, Вы угадали число!")
