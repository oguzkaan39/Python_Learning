#!usr/bin/env python
#-*-coding:utf-8-*-
#2520 sayısı 1'den 10'a kadar olan tüm sayılara kalansız bölünmektedir.
#1'den 20'ye kadar tüm sayılara kalansız bölünen ve en çok 9 basamaklı olan sayıları bulunuz.

for i in range(0,1000000000,20):
	if i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0 and i%11==0 and i%13==0 and i%14==0 and i%16==0 and i%17==0 and i%19==0:
		print(i)
	
	

	

#GELİŞTİRİLEBİLİR !