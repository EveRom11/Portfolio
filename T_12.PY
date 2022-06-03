#Программа создает массив чисел, высчитывает произведения элементов противоположных индексов 
# и складывает их в новый массив вместе с серединным значением.
import random
size=11
arr=[0]*size
for i in range(size):
    arr[i]=random.randint(1,9)
print(arr)
leN=int(len(arr)/2)
print(leN)
p=0
m=len(arr)-1
arrB=[0]*leN
k=0
while p<leN and m>leN:
    arrB[k]=arr[p]*arr[m]
    p+=1
    k+=1
    m-=1
if len(arr)%2==1:
    arrB.append(arr[leN])
else:
    arrB.pop()
print(arrB)
