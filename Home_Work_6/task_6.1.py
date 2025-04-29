# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
import string

entered_string_example_1 = "a-c"
entered_string_example_2 = "a-a"
entered_string_example_3 = "s-H"
entered_string_example_4 = "a-A"

# Example 1
start_point = string.ascii_letters.index(entered_string_example_1[0])
end_point = string.ascii_letters.index(entered_string_example_1[-1])

print(f"{entered_string_example_1} -> ", end="")
for i in range(start_point, end_point + 1):
    print(string.ascii_letters[i], end="")
print("")

# Example 2
start_point = string.ascii_letters.index(entered_string_example_2[0])
end_point = string.ascii_letters.index(entered_string_example_2[-1])

print(f"{entered_string_example_2} -> ", end="")
for i in range(start_point, end_point + 1):
    print(string.ascii_letters[i], end="")
print("")

# Example 3
start_point = string.ascii_letters.index(entered_string_example_3[0])
end_point = string.ascii_letters.index(entered_string_example_3[-1])

print(f"{entered_string_example_3} -> ", end="")
for i in range(start_point, end_point + 1):
    print(string.ascii_letters[i], end="")
print("")

# Example 4
start_point = string.ascii_letters.index(entered_string_example_4[0])
end_point = string.ascii_letters.index(entered_string_example_4[-1])

print(f"{entered_string_example_4} -> ", end="")
for i in range(start_point, end_point + 1):
    print(string.ascii_letters[i], end="")
