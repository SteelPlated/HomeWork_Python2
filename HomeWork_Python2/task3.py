'''3. Задана последовательность натуральных чисел,
завершающаяся числом 0. Требуется определить значение
второго по величине элемента в этой последовательности,
то есть элемента, который будет наибольшим, если из
последовательности удалить наибольший элемент.
Пример:
1
7
9
0
Вывод:
7
'''

first = int(input())
i = int(input())
if i > first:
    second,first = first,i
i = int(input())
while i:
    if i > first:
        second,first=first,i
    elif second<i<first:
        second=i
    i = int(input())
print(second)