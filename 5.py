n = int(input("Введите любое число: "))
revs_n = 0
while (n > 0):
    remainder = n % 10
    revs_n = (revs_n * 10) + remainder
    n = n //10
print("Обратное число от введенного: {}".format(revs_n))
