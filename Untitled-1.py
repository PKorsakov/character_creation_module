from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления '\
          'квадратного корня из заданного числа'


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    needed_value = calculate_square_root(your_number)
    if your_number <= 0:
        return 'Not exist'
    else:
        return 'Мы вычислили квадратный корень из введённого вами числа.'\
            ' Это будет: ' + str(needed_value)


print(message)
print(calc(25.5))
