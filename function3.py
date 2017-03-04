#!/usr/bin/env python
#-*- coding: utf-8 -*-
def kayit_olustur(isim,soyisim,yas,meslek):
	print("Adınız : ",isim)
	print("Soyisminiz : ",soyisim)
	print("Yasınız :",yas)
	print("Mesleğiniz : ",meslek)

isim=input("Lütfen isminizi giriniz : ")
soyisim=input("Lütfen soy isminizi giriniz : ")
yas=input("Yasınızı giriniz : ")
meslek=input("Mesleginizi giriniz : ")
kayit_olustur(isim,soyisim,int(yas),meslek)