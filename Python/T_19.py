#Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.

def count_positive_numbers(size):
    array=[0]*size
    count=0
    for i in range(size):
        array[i]=int(input("Введите целое число: "))
        if array[i]>0:
            count+=1
    print(array)
    print("Чисел больше 0 введено: ", count)

count_positive_numbers(5)