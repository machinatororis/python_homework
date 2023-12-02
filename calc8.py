import math


def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


while True:
    print("Оберіть операцію, яку потрібно виконати. \nВкажіть її лише відповідним їй числовим кодом.")
    print(
        "1 - додавання\n2 - віднімання\n3 - множення\n4 - ділення\n5 - зведення в ступінь\n6 - квадратний корінь\n7 - кубічний корінь\n0 - вихід")
    operation = int(input("Введіть номер операції: "))
    if operation == 0:
        break
    if operation == 1:
        print("Ви обрали операцію додавання.")
        print("Введіть числа для операції: ")
        a = float(input("a = "))
        b = float(input("b = "))
        result = addition(a, b)
        print(f"Результат операції = {result}")
    elif operation == 2:
        print("Ви обрали операцію віднімання.")
        print("Введіть числа для операції: ")
        a = float(input("a = "))
        b = float(input("b = "))
        result = subtraction(a, b)
        print(f"Результат операції = {result}")
    elif operation == 3:
        print("Ви обрали операцію множення.")
        print("Введіть числа для операції: ")
        a = float(input("a = "))
        b = float(input("b = "))
        result = multiplication(a, b)
        print(f"Результат операції = {result}")
    elif operation == 4:
        print("Ви обрали операцію ділення.")
        print("Введіть числа для операції: ")
        a = float(input("a = "))
        b = float(input("b = "))
        result = division(a, b)
        print(f"Результат операції = {result}")
    elif operation == 5:
        print("Ви обрали операцію зведення в ступінь.")
        print("Введіть числа для операції: ")
        a = float(input("a = "))
        b = float(input("b = "))
        result = a ** b
        print(f"Результат операції = {result}")
    elif operation == 6:
        print("Ви обрали операцію квадратний корінь.")
        print("Введіть число для операції: ")
        a = float(input("a = "))
        result = math.sqrt(a)
        print(f"Результат операції = {result}")
    elif operation == 7:
        print("Ви обрали операцію кубічний корінь.")
        print("Введіть число для операції: ")
        a = float(input("a = "))
        result = (pow(a, 1 / 3))
        print(f"Результат операції = {result}")

print(f"Робота калькулятора завершена!")
