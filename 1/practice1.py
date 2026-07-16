from random import randint

num = randint(1, 100)
user_input = int(input("Угадайте число от 1 до 100: "))
attempts = 1
while user_input != num:
    if user_input > num:
        print("меньше")
    else:
        print("больше")
    user_input = int(input("Угадайте число от 1 до 100: "))
    attempts += 1
print(f"Поздравляем! Вы угадали число за {attempts} попыток.")