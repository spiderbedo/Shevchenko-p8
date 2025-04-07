while True:
    user_input = input("Введите число: ")
    if user_input.isdigit() and user_input == str(int(user_input)):
        print(f"Введено целое число: {user_input}")
        break
    else:
        print("Ошибка. Попробуйте еще раз.")
