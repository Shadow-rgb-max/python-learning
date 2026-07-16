operation = input("Введите операцию (+, -, *, /): ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        raise ValueError("Деление на ноль невозможно.")
    result = num1 / num2
else:
    raise ValueError("Недопустимая операция.")

print(f"Результат: {result}")