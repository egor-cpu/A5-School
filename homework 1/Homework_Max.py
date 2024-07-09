import random
import datetime


input_month = int(input("Введите месяц (число от 1 до 12): "))
input_day = int(input("Введите день (число от 1 до 31): "))

month_30d = [4, 6, 9, 11]
months_31d = [1, 3, 5, 7, 8, 10, 12]

arr = []

mydates = datetime.date(2024, input_month, input_day)

for i in range(100):
    months_count = random.randint(1, 12)
    if months_count in month_30d:
        dates_count = random.randint(1, 30)
    elif months_count in months_31d:
        dates_count = random.randint(1, 31)
    else:
        dates_count = random.randint(1, 29)

    random_result = datetime.date(2024, months_count, dates_count)
    arr.append(random_result)

closest_date = min(arr, key=lambda date: abs(date - mydates))

furthest_date = max(arr, key=lambda date: abs(date - mydates))

print(f"Ближайшая дата: {closest_date}")
print(f"Самая дальняя дата: {furthest_date}")
