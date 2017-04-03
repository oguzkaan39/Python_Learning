#!usr/env/bin python
#-*- coding:utf-8 -*-i
#--------------------------SORU------------------------------
#Fibonacci dizisinin ilk 20 elemanını ekrana yazdırınız 
#KURAL 1 = Dizi yazdırılırken elle manuel olarak yazılmayacak
#For Döngüsü kullanılarak yazdırılacaktır.
#------------------------------------------------------------
fibonacci=[]
for i in range(0,20,1):
	if i==0:
		fibonacci.append(i)
	if i==1:
		fibonacci.append(i)
	if i>1:
		i=fibonacci[i-1]+fibonacci[i-2]
		fibonacci.append(i)
print("Fibonacci Dizisinin ilk 20 elemanı;\n",fibonacci)

