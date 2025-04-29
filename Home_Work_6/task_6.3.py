# Ваше завдання — написати програму, яка перемножує всі цифри,
# введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.
while True:
    try:
        number_str = input("Введіть ціле число: ")
        number = int(number_str)
        if number < 0:
            print("Будь ласка, введіть невід'ємне ціле число.")
            continue
        break
    except ValueError:
        print("Будь ласка, введіть ціле число.")

while number > 9:
    product = 1
    for digit in number_str:
        product *= int(digit)
    number = product
    number_str = str(number)

print(f"Кінцевий результат: {number}")
