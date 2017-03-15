#!/usr/bin/env/python
#-*-coding:utf-8-*-
#Bir program yazarak kullanıcıdan 10 adet sayı girmesini isteyin
#Kullanıcının aynı sayıyı birden fazla girmesine izin vermeyin.
#Girilen sayıları tek ve çift olarak ayırın ve iki liste biçiminde ekrana verin.
sayilar=[]
tekSayilar=[]
ciftSayilar=[]
while len(sayilar)<10:
	y=int(input("Sayı giriniz : "))

	if y in sayilar:
		print("Aynı rakamı giremezsiniz!")
	else:
		sayilar.append(y)
#Sayıların tek veya çift oluşunu araştırma
for i in range (0,10,1):
	if sayilar[i]%2==0:
		ciftSayilar.append(sayilar[i])
	else:
		tekSayilar.append(sayilar[i])
print("Çift Sayılar Listesi = ",ciftSayilar)
print("Tek Sayılar Listesi = ",tekSayilar)
