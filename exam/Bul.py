#!usr/env/bin python
#-*- coding:utf-8 -*-
def karsiliginibul(x,y):
	ortalama=(x+y)/2
	if 0<ortalama<25:
		print("Bu iki sayının ortalaması olan",ortalama,"nın 5'lik not karşılığı 0'dır")
	elif 25<ortalama<=44:
		print("Bu iki sayının ortalaması olan",ortalama,"nın 5'lik not karşılığı 1'dir")
	elif 44<ortalama<=54:
		print("Bu iki sayının ortalaması olan",ortalama,"nın 5'lik not karşılığı 2'dir")
	elif 54<ortalama<=69:
		print("Bu iki sayının ortalaması olan",ortalama,"nın 5'lik not karşılığı 3'tür")
	elif 69<ortalama<=84:
		print("Bu iki sayının ortalaması olan",ortalama,"nın 5'lik not karşılığı 4'tür")
	elif 84<ortalama<=100:
		print("Bu iki sayının ortalaması olan",ortalama,"nın 5'lik not karşılığı 5'tir")
	else:
		print(" ")


