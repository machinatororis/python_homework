import math

print("Оберіть операцію, яку потрібно виконати. \nВкажіть її лише відповідним їй числовим кодом.")
print("1 - додавання\n"
      "2 - віднімання\n"
      "3 - множення\n"
      "4 - ділення\n"
      "5 - зведення в ступінь\n"
      "6 - квадратний корінь\n"
      "7 - кубічний корінь\n"
      "8 - синус\n"
      "9 - косинус\n"
      "10 - тангенс")

operation = int(input("Введіть номер операції: "))

if operation == 1:
    print("Ви обрали операцію додавання.")
    print("Введіть числа для операції: ")
    a = float(input("a = "))
    b = float(input("b = "))
    result = a + b
    print(f"Результат операції = {result}")

elif operation == 2:
    print("Ви обрали операцію віднімання.")
    print("Введіть числа для операції: ")
    a = float(input("a = "))
    b = float(input("b = "))
    result = a - b
    print(f"Результат операції = {result}")
elif operation == 3:
    print("Ви обрали операцію множення.")
    print("Введіть числа для операції: ")
    a = float(input("a = "))
    b = float(input("b = "))
    result = a * b
    print(f"Результат операції = {result}")
elif operation == 4:
    print("Ви обрали операцію ділення.")
    print("Введіть числа для операції: ")
    a = float(input("a = "))
    b = float(input("b = "))
    result = a / b
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
    result = (pow(a, 1/3))
    print(f"Результат операції = {result}")
elif operation == 8:
    print("Ви обрали операцію синус.")
    print("Введіть число для операції: ")
    a = float(input("a = "))
    result = math.sin(a)
    print(f"Результат операції = {result}")
elif operation == 9:
    print("Ви обрали операцію косинус.")
    print("Введіть число для операції: ")
    a = float(input("a = "))
    result = math.cos(a)
    print(f"Результат операції = {result}")
elif operation == 10:
    print("Ви обрали операцію тангенс.")
    print("Введіть число для операції: ")
    a = float(input("a = "))
    result = math.tan(a)
    print(f"Результат операції = {result}")
else:
    print("Немає такої операції")