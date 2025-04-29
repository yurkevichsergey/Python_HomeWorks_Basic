# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
# Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів, годин, хвилин,
# а те що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)
while True:
    try:
        total_seconds = int(input("Введіть кількість секунд (від 0 до 8639999): "))
        if not 0 <= total_seconds < 8640000:
            print("Будь ласка, введіть число від 0 до 8639999.")
            continue

        days = total_seconds // (24 * 3600)
        remaining_seconds = total_seconds % (24 * 3600)
        hours = remaining_seconds // 3600
        remaining_seconds %= 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        day_word = "день"
        if days > 1 and days < 5:
            day_word = "дні"
        elif days >= 5 or days == 0:
            day_word = "днів"

        formatted_hours = str(hours).zfill(2)
        formatted_minutes = str(minutes).zfill(2)
        formatted_seconds = str(seconds).zfill(2)

        print(f"{days} {day_word}, {formatted_hours}:{formatted_minutes}:{formatted_seconds}")
        break

    except ValueError:
        print("Будь ласка, введіть ціле число.")
