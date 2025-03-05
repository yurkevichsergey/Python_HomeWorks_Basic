# Ваша програма має перенести останній елемент списку з кінця на початок, тобто,
# останній елемент списку має стати першим. Послідовність інших елементів не має змінюватися.
# Порожній список або список з одним елементом повинен залишитися незмінним.
example_list_1 = [12, 3, 4, 10]
example_list_2 = [1]
example_list_3 = []
example_list_4 = [12, 3, 4, 10, 8]

# First list example
new_list = example_list_1.copy()
if len(new_list) >= 1:
    temp = new_list[-1]
    new_list.insert(0, temp)
    del new_list[-1]
print(f"{example_list_1} => {new_list}")

# Second list example
new_list = example_list_2.copy()
if len(new_list) >= 1:
    temp = new_list[-1]
    new_list.insert(0, temp)
    del new_list[-1]
print(f"{example_list_2} => {new_list}")

# Third list example
new_list = example_list_3.copy()
if len(new_list) >= 1:
    temp = new_list[-1]
    new_list.insert(0, temp)
    del new_list[-1]
print(f"{example_list_3} => {new_list}")

# Fourth list example
new_list = example_list_4.copy()
if len(new_list) >= 1:
    temp = new_list[-1]
    new_list.insert(0, temp)
    del new_list[-1]
print(f"{example_list_4} => {new_list}")

