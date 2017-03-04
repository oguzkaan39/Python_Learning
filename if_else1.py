#!/usr/bin/env python
#-*- coding:utf-8 -*-
#if-else kullanımı
yas=int(input("Kategorinizi öğrenmek için yaşınızı giriniz : "))
if yas<=12:
	print("Çocuk Kategorisi")
elif 12<yas<=65:
	print("Yetişkin kategorisi")
else:
	print("Yaşlı kategorisi")