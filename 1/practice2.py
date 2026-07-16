shopping_list = []
while True:
    item = input("Введите товар для добавления в список покупок (или 'стоп' для завершения): ")
    if item.lower() == 'стоп':
        break
    shopping_list.append(item)

print("Список покупок:")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")