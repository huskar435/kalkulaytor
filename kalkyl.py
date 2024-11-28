def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "ошибка: деление на ноль"
def calculator():
    operation = input("Выберите операцию (+, -, *, /): ")
    num1 = float(input("Введите первое число: ").strip())
    num2 = float(input("Введите второе число: ").strip())

    if operation == '+':
        print("result:", add(num1, num2))
    elif operation == '-':
        print("result:", subtract(num1, num2))
    elif operation == '*':
        print("result:", multiply(num1, num2))
    elif operation == '/':
        print("result:", divide(num1, num2))
    else:
        print("ошибка в операции")

calculator()
