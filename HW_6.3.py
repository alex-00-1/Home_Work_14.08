# ДЗ 6.3. Добуток чисел

user_input = int(input("Enter your digit: "))
# user_input = 999 
# user_input = 1000
# user_input = 1503
# user_input = 9


if "0" in str(user_input):
    count = 0
elif user_input < 10:
    count = user_input
else:
    while int(user_input) > 10:
        count = 1

        for i in str(user_input):
            count *=  int(i)
            user_input = str(count)

print(count)