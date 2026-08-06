import pandas as pd
import numpy as np
from random import randint, shuffle
import os

FILENAME = 'data.csv' 

def random_list_with_nan(lenth: int, nans: int = 0) -> list[int, ...]:
    result: list = []
    while len(result) <= lenth - nans - 1:
        result.append(randint(40, 400))
    for _ in range(nans):
        result.append(np.nan)
    shuffle(result)
    return result
    
def generate_file(filename: str) -> bool:
    if not os.path.exists(filename):
        data = {
            'name': ['soap', 'juice', 'tomato', 'potato', 'water', 'apples', 'pears'],
            'category':  ['clean', 'drink', 'vegetables', 'vegetables', 'drink', 'fruit', 'fruit'],
            'price': random_list_with_nan(7, 2),
            'quantity': random_list_with_nan(7)
        }
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        return True
    return False

generate_file(FILENAME)
df = pd.read_csv(FILENAME)
print(f'кол-во пропусков: \n {df.isna().sum()}')
print('заполняю...')
df['price'] = df['price'].fillna(df['price'].mean())
print('успешно')
print('добавляю total')
df['total'] = df['price'] * df['quantity']
print('успешно')
df.to_csv(FILENAME, index=False)

s = df.groupby('category').agg({
    'price': 'mean',
    'total': 'sum',
    'name': 'size'
})
print('средняя цена по каждой категории:')
for category, row in s.iterrows():
    print(f"{category}: {row['price']}")
print('категория с наибольшей суммарной выручкой:')
max_category = s['total'].idxmax()
max_total = s['total'].max()
print(f'{max_category}: {max_total}')
print('товаров в каждой категории:')
for category, row in s.iterrows():
    print(f'{category}: {int(row["name"])}')