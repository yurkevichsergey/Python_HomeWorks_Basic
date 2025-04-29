# Створити клас цифрового лічильника. У класі реалізувати методи:
# встановлення максимального значення лічильника,
# встановлення мінімального значення лічильника
# встановлення початкового значення лічильника
# метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму. При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимумуʼ
# метод step_down зменшує лічильник на 1. Метод можна викликати до тих пір, поки значення не досягне мінімуму. При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
# повернення поточного значення лічильника
# Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації екземпляра класу.
# Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass
class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

    def set_min(self, min_min):
        self.min_value = min_min

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Досягнуто максимуму")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Досягнуто мінімуму")

    def get_current(self):
        return self.current

# Тести
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()
except ValueError as e:
    print(e)

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()
except ValueError as e:
    print(e)

assert counter.get_current() == 7, 'Test4'

print("OK")
