number = int(input("Введите число в секундах:"))
CONST_hour = 3600
hour = number // CONST_hour
hour_min = number % CONST_hour
CONST_min = 60
minute = hour_min // CONST_min
second = hour_min % CONST_min
print(f"{hour:02d}:{minute:02d}:{second:02d}")
