# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
import random

for _ in range(4):
    new_list = []
    random_list = []
    for count in range(random.randint(3, 10)):
        random_list.append(random.randint(1, 10))
        if count == 0 or count == 2:
            new_list.append(random_list[count])
    new_list.append(random_list[-1])
    print(f"{random_list} == {new_list}")
