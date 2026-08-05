import numpy as np

a = np.array([i for i in range(1, 21)])
print(a.shape, a.dtype)

a = a.reshape(4, 5)

print(f'первая строка: {a[0, :]}')
print(f'последний столбец: {a[:, -1]}')

print(f'элемент в 2 строке и 3 столбце: {a[1, 2]}')

print(a.sum(axis=1))
print(a.sum(axis=0))