#!usr/bin/env python
#-*- coding:utf-8 -*-
#Girilen sayının asal olup olmadığını bulan programı yazınız !
#Eğer girilen sayının 2'den fazla böleni varsa Asal DEĞİLDİR!
#Eğer girilen sayının 2'den fazla böleni yoksa ASALDIR!
sayi=int(input("Bir sayi giriniz : "))
bolum=0
#Sayının kaç tane böleni olduğunu öğren
for i in range (1,sayi,1):
	if sayi%i==0 and sayi%sayi==0 :
		bolum+=1
#Bölen sayısına göre girilen sayının asallığını araştır.
if bolum>=2:
	print("Asal değildir.")
if bolum<2:
	print("Asaldır")
	