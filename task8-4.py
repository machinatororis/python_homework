def avg(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)

while True:
    print("Введіть три числа або 0 для виходу")
    a = int(input("Введіть перше число (або 0 для виходу): "))
    b = int(input("Введіть друге число (або 0 для виходу): "))
    c = int(input("Введіть третє число (або 0 для виходу): "))
    if a == 0 or b == 0 or c == 0:
        break
    result = avg(a, b, c)
    print(f"Середнє арифметичне: {result:.2f}")

print(f"Робота завершена!")