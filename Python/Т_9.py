#Программа принимает число с клавиатуры и  проверяет, является ли оно пaлиндромом.
print("Введите число для проверки")
number=str(input())
len=len(number)
l=int(len/2)
minus_index=l-1
plus_index=l+1
step=0
if len%2==0:
    plus_index-=1
while minus_index>=0:
    if number[minus_index]==number[plus_index]:
        minus_index-=1
        plus_index+=1
        step+=1
    else:
        break
if number=="":
    print("Все пошло не так")
elif l>step or len==1:
    print("Число не является палиндромом")
elif l==step:
    print("Число является палиндромом")
 