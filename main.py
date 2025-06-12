import random

print("Вітаю, Друже у грі 'Вгадай число'.")
print("Правила гри дуже прості: я загадую ціле число від 1 до 100, а ти маєш за 5 спроб його вгадати.")
print("Бажаю успіхів!\n")

# Программа загадывает случайное число
secret_number = random.randint(1, 100)

# Игрок получает 5 попыток
for attempt in range(1, 6):
    guess_input = input(f"Спроба №{attempt}. Введіть ваше число: ")

    try:
        guess = int(guess_input)
    except ValueError:
        print("Це не ціле число! Спроба не зараховується.\n")
        continue  # переход к следующей попытке

    if guess == secret_number:
        print(f"\n🎉 Вітаю! Ви вгадали число {secret_number} з {attempt} спроби!")
        break
    elif guess < secret_number:
        print("Загадане число більше.\n")
    else:
        print("Загадане число менше.\n")
else:
    # Если игрок не угадал ни разу
    print(f"\n😢 Ви програли. Загадане число було: {secret_number}")