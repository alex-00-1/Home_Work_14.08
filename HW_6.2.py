# ДЗ 6.2. Конвертер із числа в дату

# 224930 -> 2 дні, 14:28:50

input_seconds = int(input("Enter seconds value: "))
# input_seconds = 86_400
# input_seconds = 8_639_999
# input_seconds = 8_640_001



if 0 <= input_seconds <= 8_640_000:

    days = input_seconds // 60 ** 2 // 24

    if days % 10 == 1:
        day_name = "день"
    elif days % 10 in [2, 3, 4,]:
        day_name = "дні"
    else:
        day_name = "днів"

    hours = str(input_seconds // 60 ** 2 % 24).zfill(2)
    minutes = str(input_seconds // 60 % 60).zfill(2)
    seconds = str(input_seconds % 60).zfill(2)

    print(f"{days} {day_name}, {hours}:{minutes}:{seconds}")

else:
    print("Too large value")
