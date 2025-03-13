# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
#    починатися з цифри
#    містити великі літери,
#    пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
#    бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
import keyword
import string
from string import punctuation

variable_test = ['_', '__', '___', 'x', 'get_value',
                 'get value', 'get!value', 'some_super_puper_value', 'Get_value', 'get_Value',
                 'getValue' ,'3m', 'm3', 'assert', 'assert_exception']

punctuation_list = list(string.punctuation)
del punctuation_list[punctuation_list.index('_')]
punctuation_list.append(' ')

for i in range(len(variable_test)):
    if variable_test[i] in keyword.kwlist:
        print(f"{variable_test[i]} => False")
        continue

    elif any(char.isupper() for char in variable_test[i]):
        print(f"{variable_test[i]} => False")
        continue

    elif variable_test[i][0].isnumeric():
        print(f"{variable_test[i]} => False")
        continue

    elif any(char in punctuation_list for char in variable_test[i]):
        print(f"{variable_test[i]} => False")
        continue

    elif (variable_test[i] == '_' * len(variable_test[i])) and len(variable_test[i]) > 1:
        print(f"{variable_test[i]} => False")
        continue

    else:
        print(f"{variable_test[i]} => True")
        continue
