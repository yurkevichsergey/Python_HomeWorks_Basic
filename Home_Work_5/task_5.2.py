# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора
# після кожного обчислення - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
import os

while True:

    while True:
        first_number = input("Enter the first number: ")
        if first_number.isnumeric():
            first_number = int(first_number)
            break
        else: print("Error. Please enter the number!")

    while True:
        second_number = input("Enter the second number: ")
        if second_number.isnumeric():
            second_number = int(second_number)
            break
        else: print("Error. Please enter the number!")

    while True:
        math_operator = input("Choose math action (+, -, *, /): ")
        if math_operator in ('+', '-', '*', '/'):
            break
        else: print("Error. Please enter the correct math action!")

    match math_operator:
        case '+':
            result = first_number + second_number
        case '-':
            result = first_number - second_number
        case '*':
            result = first_number * second_number
        case '/':
            if second_number == 0:
                result = "Error, division by zero!"
            else:
                result = first_number / second_number
        case _:
            result = "N/A"

    print(f"{first_number} {math_operator} {second_number} = {result}")

    confirm_calculation = input("Start next calculation? Enter 'yes' or 'y' to continue: ")
    if confirm_calculation.lower() not in ('yes', 'y'):
        break
    else:
        print('-' * 40)
