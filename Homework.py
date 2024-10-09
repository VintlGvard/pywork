# Задача на проверку простоты числа: Напишите программу, которая принимает на вход число и определяет, является ли оно простым. (без встроенных функций)
""" Задача 1
number = int(input("Введите число: "))
def numb(number):
    count = 0
    for i in range(1, 51):
        if number % i == 0:
            count += 1 
    if count > 2:
        print("Сложное")
    else:
        print("Простое")
numb(number)
"""
# Задача о сортировке массива: Напишите программу, которая принимает на вход массив чисел и сортирует его по возрастанию. (без встроенных функций)
""" Задача 2
arr = [1, 2, 5, 2, 7, 8, 11, 25, 72, 2, 5, 32]
def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(sort(arr))
"""
# Задача о поиске наибольшего элемента в массиве: Напишите программу, которая принимает на вход массив чисел и находит наибольший элемент в этом массиве. (без встроенных функций)
""" Задача 3
list1 = [1,4,5,2,6,2,3,1,5,8]
def maxlist(list1): 
    maxx = list1[0]
    for i in list1:
        if i > maxx:
           maxx = i
    return maxx
print(maxlist(list1))
"""
# Задача о вычислении числа Фибоначчи: Напишите программу, которая принимает на вход номер числа Фибоначчи и выводит само число. (без встроенных функций)
""" Задача 4
n = int(input("Введите число: "))
def fib(n):
    if n == 1:
        return n 
    elif n == 0:
        return 0 
    elif n>1:
        return fib(n-1)+fib(n-2)
print(fib(n))
"""
# Задача на хэш-таблицы: Напишите программу, которая принимает на вход массив строк и выводит наиболее часто встречающуюся строку. (без встроенных функций)
""" Задача 5
text = input("Введите слова через пробел: ")
def found_text(text:str):
    text = text.split(" ")
    maxx_count = 0
    maxx_count_word = ""
    for i in text:
        if maxx_count<text.count(i):
            maxx_count = text.count(i)
            maxx_count_word = i
    return maxx_count_word
print(found_text(text))
"""