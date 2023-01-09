"""
Домашнее задание №1
Функции и структуры данных
"""
import random


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda number: number * number, numbers))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    if number <= 1:
        return False
    k = 10 #тест Ферма с k проходами, вероятность ошибки 0,0009765625
    for i in range(k):
        random.seed()
        rand_number = random.randint(1, number-1)
        if (rand_number ** (number - 1)) % number != 1:
            return False
    return True

def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda number: number % 2 != 0, numbers))
    if filter_type == EVEN:
        return list(filter(lambda number: number % 2 == 0, numbers))
    if filter_type == PRIME:
        return list(filter(is_prime, numbers))