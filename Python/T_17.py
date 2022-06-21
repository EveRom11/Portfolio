#Задача 36: Задайте одномерный массив, заполненный случайными числами.
# Найдите сумму элементов, стоящих на нечётных позициях.

def sum_odd_indexes(size):
    import random
    array=[0]*size
    sum=0
    for i in range(size):
        array[i]=random.randint(1,21)
        if i%2==1:
            print(i)
            sum+=array[i]
    print(array)
    print("Сумма чисел под нечетными индексами: ", sum)

sum_odd_indexes(15)