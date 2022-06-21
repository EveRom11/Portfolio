#Задача 27: Напишите функцию, которая принимает на вход число и выдаёт сумму цифр в числе.

def scalpel(num):
    num=str(num)
    sum=0
    for i in range(len(num)):
        sum+=int(num[i])
    print(sum)  
       


scalpel(452)