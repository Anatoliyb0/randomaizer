import random
import time

def get_number_input(prompt="Введите число: "):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
            print("Ошибка! Ввод не может быть пустым.")
            continue

        try:
            return int(user_input)
        except ValueError:
            print("Ошибка! Введите целое число.")


def get_boolean_input(prompt):
    while True:
        answer = input(prompt + " (д/н): ").lower()
        if answer in ['д', 'да', 'yes', 'y']:
            return True
        elif answer in ['н', 'нет', 'no', 'n']:
            return False
        else:
            print("Пожалуйста, ответьте д (да) или н (нет)")


def calculate_score(start_capital, attempts_used, elapsed_time):
    score = start_capital

    for i in range(attempts_used):
        score = score - (score * 0.1)

    score = score - elapsed_time

    if elapsed_time <= 10:
        score = score * 2
        print("Бонус за скорость! Счет удвоен.")

    return max(0, round(score, 2))


def play_game():

    print("НАСТРОЙКА ИГРЫ")

    # Настройка диапазона
    a = get_number_input("Введите минимальное число: ")
    b = get_number_input("Введите максимальное число: ")

    if a > b:
        print("Ошибка!")
        a, b = b, a

    max_attempts = get_number_input("Введите максимальное количество попыток: ")

    hints = get_boolean_input("Включить подсказки? ")

    start_capital = get_number_input("Сколько очков? ")

    secret = random.randint(a, b)

    print("\n" + "=" * 50)
    print(f"Число загадано! (от {a} до {b}). Осталось: {max_attempts} попыток")

    start_time = time.time()

    attempts_left = max_attempts
    attempts_used = 0
    won = False

    while attempts_left > 0 and not won:
        print(f"\nОсталось попыток: {attempts_left}")

        guess = get_number_input("Ваша догадка: ")

        if guess < a or guess > b:
            print(f"Число должно быть от {a} до {b}!")
            continue

        attempts_left -= 1
        attempts_used += 1

        if guess == secret:
            won = True
            break

        if hints:
            if guess < secret:
                print(f"Загаданное число больше {guess}")
            else:
                print(f"Загаданное число меньше {guess}")
        else:
            print("Неверно!")

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    print("\n" + "=" * 50)

    if won:
        final_score = calculate_score(start_capital, attempts_used, elapsed_time)

        print("ПОБЕДА!")
        print(f"Число: {secret}")
        print(f"Время: {elapsed_time} сек")
        print(f"Попыток использовано: {attempts_used}")
        print(f"Итоговый счет: {final_score}")
    else:
        print(f"Проигрыш! Число было: {secret}")
        print(f"Время: {elapsed_time} сек")
        print(f"Итоговый счет: 0")

    return won


def main():
    print("Добро пожаловать в игру")

    while True:
        play_game()

        # Спрашиваем, хочет ли пользователь сыграть еще
        again = get_boolean_input("\nХотите сыграть еще?")
        if not again:
            print("\nСпасибо за игру! До свидания!")
            break


main()