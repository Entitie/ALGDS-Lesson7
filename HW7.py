# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
import timeit


def bubble_sort(our_arr):
    a = our_arr
    for k in range(len(a) - 1, 0, -1):
        for i in range(k):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
        # print(a)
    return a


def random_numbers(amount, edge):
    numbers = []
    for _ in range(amount):
        numbers.append(randint(-edge, edge))
    return numbers


amount = int(input('Введите количество чисел: '))
edge = int(input('Введите число границу диапазона: '))

unsort_numbers = random_numbers(amount, edge)
print(f'Числа до сортировки: {unsort_numbers}')
numbers = bubble_sort(unsort_numbers)
print(f'Числа после сортировки {numbers}')

# Во время просмотра записи пришла идея алгоритма найти максимум или минимум и перенести значние в другой массив


def my_sort(array, amount):
    in_arr = array
    out_arr = []
    for _ in range(amount):
        min_index = 0
        min = in_arr[min_index]
        for el in range(len(in_arr)):
            if min > in_arr[el]:
                min_index = el
        out_arr.append(in_arr.pop(min_index))
        # print(in_arr)
        # print(out_arr)
    return out_arr


my_numbers = my_sort(unsort_numbers, amount)
print(f'Числа после моей сортировки {my_numbers}')
