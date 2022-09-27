import random
temps = [[random.uniform(10.0,30.0) for h in range(24)] for d in range(30)]
average = []
varninday = 0
for day in temps:
    average.append(round(sum(day)/24, 1))
print(temps)
print(average)
print("Средняя температура:", round(sum(average)/30, 1))
