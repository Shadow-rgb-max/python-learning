def calculate(operation, num1, num2):
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            return "Недопустимая операция."
        return result
    except ZeroDivisionError:
        raise ValueError("Деление на ноль невозможно.")
    
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введено не число. Попробуй снова.")


operation = input("Введите операцию (+, -, *, /): ")
num1 = get_number("Введите первое число: ")
num2 = get_number("Введите второе число: ")



try:
    result = calculate(operation, num1, num2)
    print(f"Результат: {result}")
except ValueError as e:
    print(f"Ошибка: {e}")

