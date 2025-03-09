# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!
example_list_1 = [0, 1, 0, 12, 3]
example_list_2 = [0]
example_list_3 = [1, 0, 13, 0, 0, 0, 5]
example_list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

# First list
zero_count = example_list_1.count(0)
if len(example_list_1) > 1:
    for _ in range (zero_count):
        zero_index = example_list_1.index(0)
        del example_list_1[zero_index]
        example_list_1.append(0)

print(f"{[0, 1, 0, 12, 3]} -> {example_list_1}")

# Second list
zero_count = example_list_2.count(0)
if len(example_list_2) > 1:
    for _ in range (zero_count):
        zero_index = example_list_2.index(0)
        del example_list_2[zero_index]
        example_list_2.append(0)

print(f"{[0]} -> {example_list_2}")

# Third list
zero_count = example_list_3.count(0)
if len(example_list_3) > 1:
    for _ in range (zero_count):
        zero_index = example_list_3.index(0)
        del example_list_3[zero_index]
        example_list_3.append(0)

print(f"{[1, 0, 13, 0, 0, 0, 5]} -> {example_list_3}")

# Fourth list
zero_count = example_list_4.count(0)
if len(example_list_4) > 1:
    for _ in range (zero_count):
        zero_index = example_list_4.index(0)
        del example_list_4[zero_index]
        example_list_4.append(0)

print(f"{[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]} -> {example_list_4}")

