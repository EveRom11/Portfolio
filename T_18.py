#Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.

def array_maker(size):
    import random
    array=[0]*size
    for i in range(size):
        array[i]=float(random.randint(1,21))
    return array

def diff_indexes(array):
    min=array[0]
    max=array[0]
    for i in range(1,len(array)):
        if array[i]>max:
            max=array[i]
        elif array[i]<min:
            min=array[i]
    print(array)
    print(max)
    print(min)
    print("Разница между максимальным и минимальным элементами массива: ", max-min)

diff_indexes(array_maker(15))