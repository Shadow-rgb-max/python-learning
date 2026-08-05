import numpy as np

temperatures_celsius = np.array([0, 32, -5, 28, 31, 9, 33, 19, 25, -10])
temperatures_fahrenheit = temperatures_celsius * 9/5 + 32

print("максимальная температура в фаренгейтах:", np.max(temperatures_fahrenheit))
print("минимальная температура в фаренгейтах:", np.min(temperatures_fahrenheit))
print("средняя температура в фаренгейтах:", np.mean(temperatures_fahrenheit))
print("стандартное отклонение температуры в фаренгейтах:", np.std(temperatures_fahrenheit))
temperature_more_than_15 = temperatures_celsius[temperatures_celsius > 15]
print('дни, когда температура была выше 15 градусов по цельсию:', temperature_more_than_15)
print('количество таких дней:', temperature_more_than_15.size)
