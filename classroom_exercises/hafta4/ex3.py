#!/usr/bin/env python
#-*-coding:utf-8-*-
#TC kimlik numarası doğrulugunu test eden program : 
tc=input("Tc Kimlik Giriniz : ")
toplam=0
if len(tc)==11 and int(tc)>0 and tc.isdigit()==True:
	toplam1=int(tc[0])+int(tc[2])+int(tc[4])+int(tc[6])+int(tc[8])
	toplam2=int(tc[1])+int(tc[3])+int(tc[5])+int(tc[7])
	kural1=(toplam1*7-toplam2)%10
	for i in range(0,10,1):
		toplam=toplam+int(tc[i])
	kural2=toplam%10
	if kural1==int(tc[9]) and kural2==int(tc[10]) and int(tc[0])!=0:
		print("Girilen tc geçerlidir.")
	else:
		print("Girilen tc geçersizdir.")
else:
	print("Lütfen 11 basamaklı bir tamsayı giriniz.")
	