while True:
    height = input("Введіть ваш зріст (у метрах) у форматі 0.00 м або off для виходу ").lower()
    weight = input("Введіть вашу вагу (у кг) у форматі 0.00 кг або off для виходу ").lower()

    if height == "off" or weight == "off":
        break

    # Preparation
    height = height.translate(
        str.maketrans(",", ".", " ")
    )
    weight = weight.translate(
        str.maketrans(",", ".", " ")
    )

    height = float(height)
    weight = float(weight)
    imt = weight/(height * height)
    print(f"Ваш зріст: {height}\nВаша вага: {weight}\nВаш ІМТ: {imt}")

    if imt < 18.5:
        print("Недостатня вага!")
    elif imt > 25:
        print("Слідкуйте за фігурою!")
    else:
        print("Маса тіла в нормі :)")
