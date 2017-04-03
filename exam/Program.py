#!usr/env/bin python
#-*- coding:utf-8 -*-
#---------------------------------SORU----------------------------------
#Dışarıdan girilen 2 notun 5 lik not sistemindeki karşılığını yazdırınız.
#KURAL = İstenilen durum tek bir dosyada yazılmayacaktır.
#		 Bul.py dosyasında karşılığını bulan bir modül yazılacak ve
#		 Program.py dosyasında sadece kullanıcıdan not alma işlemi yapılacaktır.
#		 Diğer tüm işlemler kendi yazdığınız modülde gerçekleştirilecektir.
#-----------------------------------------------------------------------
import Bul
not1=int(input("Birinci notu giriniz : "))
not2=int(input("İkinci notu giriniz: "))
print(Bul.karsiliginibul(not1,not2))