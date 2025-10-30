while True: # Бесконечный цикл True
    try: # Нужен для бесконечного цикла
        user_number = int(input("Your first number:")) # Первое число от пользователя
        user_operation = input("Your operation (+, -, /, *, or q to quit):") # Пользователь выбирает операцию, или q (выход)
        if user_operation == "q": # Если пользователь выбирает q - программа останавливается
            break # Сама "остановка"
        elif user_operation == "+": # Пользователь выбрал операцию "+"
            user_second_number = int(input("Your second number:")) # Просим пользователя ввести 2 число для операции. Это можно сделать вне этого цикла
            result = user_number + user_second_number # Переменная результата
            print("Your result is:" + str(result)) # Обозначаем результат
        elif user_operation == "-": # Пользователь выбрал операцию "-"
            user_second_number = int(input("Your second number:")) # Просим пользователя ввести 2 число для операции. Это можно сделать вне этого цикла
            result = user_number - user_second_number # Переменная результата
            print("Your result is:" + str(result)) # Обозначаем результат
        elif user_operation == "/": # Пользователь выбрал операцию "/"
            user_second_number = int(input("Your second number:")) # Просим пользователя ввести 2 число для операции. Это можно сделать вне этого цикла
            if user_second_number == 0: # Блок проверки на 0 при делении ("/")
                print("Your second number is 0") # Сообщение пользователю об его ошибке
                continue # Запуск заново, так как была ошибка
            else: # В случае, если second_number != 0
                result = user_number / user_second_number # Переменная результата
                print("Your result is:" + str(result)) # Обозначаем результат
        elif user_operation == "*": # Пользователь выбрал операцию "*"
            user_second_number = int(input("Your second number:")) # Просим пользователя ввести 2 число для операции. Это можно сделать вне этого цикла
            result = user_number * user_second_number # Переменная результата
            print("Your result is:" + str(result)) # Обозначаем результат
    except ValueError: # Нужен для бесконечного цикла
        print("Invalid input") # Нужен для бесконечного цикла

