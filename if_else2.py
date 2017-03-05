#!/usr/bin/env python
#-*- coding: utf-8 -*-
note = int(input("Notunuzu Giriniz : "))
#note değişkeni 0 ve 50 arasında mı?
#50 dahil midir?
#50 dahil değildir! (0,50)'nin matematiksel karşılığı = [0,50) dir.
if note in range(0,50):
	print("Kaldınız ")

else:
	print("Geçtiniz")