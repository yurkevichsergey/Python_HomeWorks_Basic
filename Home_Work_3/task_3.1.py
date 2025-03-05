# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії,
# обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
math_operator = input("Choose math action (+, -, *, /): ")

match math_operator:
    case '+':
        result = first_number + second_number
        print(result)
    case '-':
        result = first_number - second_number
        print(result)
    case '*':
        result = first_number * second_number
        print(result)
    case '/':
        if second_number == 0:
            print("Error, division by zero!")
        else:
            result = first_number / second_number
            print(result)
    case _:
        print("Error, please choose valid math action")
