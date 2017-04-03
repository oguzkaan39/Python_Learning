#!usr/env/bin python
#-*- coding:utf-8 -*-
#---------------------------SORU---------------------------------------------------
#Bilgisayarın rastgele tuttuğu bir sayıyı tahmin etme oyunu yazınız.
#KURAL = Kullanıcı 4 defa yanlış girdiğinde BAŞARISIZ sayılacaktır.
#KURAL2 = Örneğin bilgisayarın tuttuğu sayı 5 olsun
#		  Kullanıcı 5 sayınının 2 düşüğünü ya da 2 fazlasını girdiğinde
#		  BAŞARILI sayılacaktır(3,4,5,6,7). Yani Kullanıcının +-2 toleransı vardır.
#Yukarıdaki kurallara uyarak programı yazınız.
#----------------------------------------------------------------------------------
import random
sayi=random.randint(0,10)
hata=1
while True:
	tahmin=int(input("Sayiyi tahmin ediniz : "))
	if tahmin==sayi-1 or tahmin==sayi-2 or tahmin==sayi+1 or tahmin==sayi+2 or tahmin==sayi:
		print(" oyuncu oyunu oynadı ve BAŞARILI oldu")
		print("Tutulan sayı : ",sayi)
		break
	else:
		print("BAŞARISIZ")
		print("Tutulan sayı : ",sayi)
		if hata==4:
			print("4 defa hatalı tahmin ettiğiniz için BAŞARISIZ sayıldınız")
			break
		hata+=1
