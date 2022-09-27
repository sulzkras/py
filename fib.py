#  def powof2(n):
#      pow = 1
#      for i in range(n):
#          yield pow
#          pow *= 2
#
# for v in powof2(10):
#     # print(v)
#
# list1 = [x for x in powof2(10)]
# print(list1)
# list2 = list1(powof2(10))
# print(list2)

# def Fib(n):
#     p1 = p2 = 1
#     for i in range(n):
#         if i in [0, 1]:
#             yield 1
#         else:
#             n = p1 + p2
#             p2, p1 = p1, n
#             yield n
#
# fibsChesl = list(Fib(10))
# print(fibsChesl)

# list1 =[]
# for i in range(8):
#     list1.append(i ** 10)
#
# list2 = [i ** 10 for i in range(8)]
# print(list1)
# print(list2)


# list1 =[]
# for i in range(8):
#     list1.append(1 if i % 2 ==0 else 0)
# print(list1)
#
# list2 = [1 if i % 2 ==0 else 0 for i in range(8)]
# print(list2)



# list1 = (1 if i % 2 ==0 else 0 for i in range(8))
# list2 = [1 if i % 2 ==0 else 0 for i in range(8)]
# for i in list2:
#     print(i, end = " ")
# print()
# for i in list1:
#     print(i, end = " ")
# print()
# print(len(list2))
# print(len(list1))

# lambda param: exp
# one = lambda: 3
# x2 = lambda x: x*x
# pwr = lambda x, y: x*y
#
#                                                                                                                                        for i in range(-4, 2):
#     print(x2(i), end = " ")
#     print(pwr(i, one()), end = " ")

# def poly(x):
#     return 2 * x ** 2 - 4 * x - 2
# def printf(args, fun):
#     for i in args:
#         print("f(", i, ")=", fun(i), sep="")
# if __name__ == "__main__":
#     print([i for i in range(-5, 5)], poly)
#     print([i for i in range(-5, 5)], lambda i: 2 * x ** 2 - 4 * x - 2)
