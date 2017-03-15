#!/usr/bin/env/python
#-*-coding:utf-8-*-
#Rakamlar isimli bir liste oluşturulacak. Bu listede 0-9 arası rakamlar olacaktır. 
#Dışarıdan bir değer girilecek. 
#Eğer girilen değer listede varsa «Evet bu bir rakamdır» yoksa «Hayır bu bir rakam değildir» yazılacaktır.
rakamlar=[0,1,2,3,4,5,6,7,8,9]
x=int(input("Sayı giriniz : "))
if rakamlar.count(x)==True:
	print("Evet bu bir rakamdır.")
else:
	print("Bu bir rakam değildir.")

