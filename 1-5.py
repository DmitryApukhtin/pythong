dohod = int(input("Введите прибыль: "))
rashod = int(input("Введите расходы: "))
if dohod > rashod:
    profit = dohod-rashod
    rent = dohod/rashod
    print(f"Рентабельность = {rent}")
    rab = int(input("Количество работников: "))
    print(f"Прибыль {profit/rab} на работника")
elif dohod == rashod:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток ")
