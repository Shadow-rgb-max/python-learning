import datetime

name = input("ваше имя: ")
age = int(input("ваш возраст: "))

current_year = datetime.datetime.now().year
year_100 = current_year + (100 - age)
print(f"{name}, тебе исполнится 100 лет в {year_100} году.")
