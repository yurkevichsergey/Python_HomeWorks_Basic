# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
# Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.
example_list_1 = [1, 2, 3, 4, 5 ,6]
example_list_2 = [1, 2, 3]
example_list_3 = [1, 2, 3, 4, 5]
example_list_4 = [1]
example_list_5 = []

# First list example
if len(example_list_1) >= 2:
    count_elements_first_list = len(example_list_1) // 2
    new_list = [example_list_1[:count_elements_first_list], example_list_1[count_elements_first_list:]]
elif len(example_list_1) == 1:
    new_list = [example_list_1[:], []]
else:
    new_list = [[], []]
print(f"{example_list_1} => {new_list}")

# Second list example
if len(example_list_2) >= 2:
    count_elements_first_list = len(example_list_2) // 2
    new_list = [example_list_2[:count_elements_first_list], example_list_2[count_elements_first_list:]]
elif len(example_list_2) == 1:
    new_list = [example_list_2[:], []]
else:
    new_list = [[], []]
print(f"{example_list_2} => {new_list}")

# Third list example
if len(example_list_3) >= 2:
    count_elements_first_list = len(example_list_3) // 2
    new_list = [example_list_3[:count_elements_first_list], example_list_3[count_elements_first_list:]]
elif len(example_list_3) == 1:
    new_list = [example_list_3[:], []]
else:
    new_list = [[], []]
print(f"{example_list_3} => {new_list}")

# Fourth list example
if len(example_list_4) >= 2:
    count_elements_first_list = len(example_list_4) // 2
    new_list = [example_list_4[:count_elements_first_list], example_list_4[count_elements_first_list:]]
elif len(example_list_4) == 1:
    new_list = [example_list_4[:], []]
else:
    new_list = [[], []]
print(f"{example_list_4} => {new_list}")

# Fifth list example
if len(example_list_5) >= 2:
    count_elements_first_list = len(example_list_5) // 2
    new_list = [example_list_5[:count_elements_first_list], example_list_5[count_elements_first_list:]]
elif len(example_list_5) == 1:
    new_list = [example_list_3[:], []]
else:
    new_list = [[], []]
print(f"{example_list_5} => {new_list}")
