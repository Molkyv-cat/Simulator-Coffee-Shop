print("--- Симулятор заказа в кофейне ---")

price = int()

one_choise = input("Введите ваш выбор (Кофе/Чай/Какао/Лимонад): ")

if one_choise == "Кофе":
    price = price + 90

    two_choise = input("Отличный выбор! Какой размер вам нужен (Маленький/Средний/Большой)?: ")
    if two_choise == "Маленький":
        price = price + 10
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Средний":
        price = price + 25
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Большой":
        price = price + 50
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    else:
        print("Неверный выбор!")

elif one_choise == "Чай":
    price = price + 70

    two_choise = input("Отличный выбор! Какой размер вам нужен (Маленький/Средний/Большой)?: ")

    if two_choise == "Маленький":
        price = price + 10
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Средний":
        price = price + 25
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Большой":
        price = price + 50
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    else:
        print("Неверный выбор!")
elif one_choise == "Какао":
    price = price + 80

    two_choise = input("Отличный выбор! Какой размер вам нужен (Маленький/Средний/Большой)?: ")

    if two_choise == "Маленький":
        price = price + 10
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Средний":
        price = price + 25
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Большой":
        price = price + 50
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    else:
        print("Неверный выбор!")
elif one_choise == "Лимонад":
    price = price + 75

    two_choise = input("Отличный выбор! Какой размер вам нужен (Маленький/Средний/Большой)?: ")

    if two_choise == "Маленький":
        price = price + 10
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Средний":
        price = price + 25
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    elif two_choise == "Большой":
        price = price + 50
        card = input("Еще чуть-чуть! У вас есть карта лояльности? (Да/Нет): ")
        if card == "Да":
            price = price - 5
            print(f"Отлично! Цена будет: {price}руб.")
        elif card == "Нет":
            print(f"Хорошо! Цена будет {price}руб.")
        else:
            print("Неверный выбор!")
    else:
        print("Неверный выбор!")

else:
    print("Неверный выбор попробуете еще раз!")