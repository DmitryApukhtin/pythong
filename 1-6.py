x = int(input("Введите первый результат" ))
y = int(input("Введите желаемый результат" ))
i = 1
while x < y:
    x *= 1.1
    i += 1
print("Вы достигнете желаемый резултат за", i , "дней")