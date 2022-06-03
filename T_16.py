#Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. 
#Напишите программу, которая покажет количество чётных чисел в массиве.

def count_even_numbers(size):
    import random
    array=[0]*size
    even=0
    for i in range(size):
        array[i]=random.randint(100,1000)
        if array[i]%2==0:
            even+=1
    print(array)
    print("Четных чисел в массиве ",even)

count_even_numbers(15)