# Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів цього класу.
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можна множити тільки на об'єкт класу Fraction")
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можна додавати тільки об'єкти класу Fraction")
        new_a = self.a * other.b + self.b * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можна віднімати тільки об'єкти класу Fraction")
        new_a = self.a * other.b - self.b * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.a * other.b == other.a * self.b

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18', f"Очікувалось: Fraction: 21, 18, отримано: {str(f_c)}"

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18', f"Очікувалось: Fraction: 6, 18, отримано: {str(f_d)}"

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18', f"Очікувалось: Fraction: 3, 18, отримано: {str(f_e)}"

assert f_d < f_c, "f_d має бути менше за f_c"
assert f_d > f_e, "f_d має бути більше за f_e"
assert f_a != f_b, "f_a має бути не рівним f_b"

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2, "f_1 має бути рівним f_2"

print('OK')
