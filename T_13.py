#Задача 25: Напишите (функцию) цикл, 
# который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
def pow_1(a,b):
    result=1
    k=0
    while k<b:
        result=result*a
        k+=1
    print(result)

pow_1(2,3)