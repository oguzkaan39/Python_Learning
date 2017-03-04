#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Topla fonksiyonu
def topla(a,b):
	
	return a+b
#Kullanıcıdan integer tipinde bir veri almak
sayi1=int(input("Birinci değeri giriniz : "))
sayi2=int(input("İkinci değeri girininiz : "))
#print fonksiyonu içinde topla fonksiyonunun çağırılması.
print("Toplam = ",topla(int(sayi1),int(sayi2)))