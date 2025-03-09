# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.
# Не забудьте, що перший елемент масиву має індекс 0.
# Для порожнього масиву результат завжди 0.
example_list_1 = [1, 3, 5]
example_list_2 = [6]
example_list_3 = []
example_list_4 = [0, 1, 7, 2, 4, 8]

# First example
summary = 0
if len(example_list_1) > 1:
    for count in range(len(example_list_1)):
        if count % 2 == 0 or count == 0:
            summary += example_list_1[count]
    summary *= example_list_1[-1]

elif len(example_list_1) == 1:
    summary = example_list_1[-1] * example_list_1[-1]

print(f"{example_list_1} => {summary}")


# Second example
summary = 0
if len(example_list_2) > 1:
    for count in range(len(example_list_2)):
        if count % 2 == 0 or count == 0:
            summary += example_list_2[count]
    summary *= example_list_2[-1]

elif len(example_list_2) == 1:
    summary = example_list_2[-1] * example_list_2[-1]

print(f"{example_list_2} => {summary}")


# Third example
summary = 0
if len(example_list_3) > 1:
    for count in range(len(example_list_3)):
        if count % 2 == 0 or count == 0:
            summary += example_list_3[count]
    summary *= example_list_3[-1]

elif len(example_list_3) == 1:
    summary = example_list_3[-1] * example_list_3[-1]

print(f"{example_list_3} => {summary}")


# Fourth example
summary = 0
if len(example_list_4) > 1:
    for count in range(len(example_list_4)):
        if count % 2 == 0 or count == 0:
            summary += example_list_4[count]
    summary *= example_list_4[-1]

elif len(example_list_4) == 1:
    summary = example_list_4[-1] * example_list_4[-1]

print(f"{example_list_4} => {summary}")
