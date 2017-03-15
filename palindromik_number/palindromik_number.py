#!/usr/bin/env/python
#-*-coding:utf-8-*-
#Palindromik sayı, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılardır.
#Örneğin 54245 sayısı palindromik sayıdır.
#5 Rakamlı girilen bir sayının palindromik  sayı olup olmadığını bulunuz(palindromik_number.py)
#-----------------------------------------------------------------------------------------------------
#Sayının herhangi bir basamağını ekrana yazdırmak .
#x="54245"
#print("Sayının birler basamağı : ",x[4])
#-----------------------------------------------------------------------------------------------------
def enterNumber():
	global number
	number=input("Bir sayı giriniz : ")
	lenght()
def testNumber():
	#5 basamaklı sayının palindromik sayı olması için ilk 2 ve son2 rakamın aynı olması lazım
	#Yani number[0]==number[4] and number[1]==number[3]
	if number[0]==number[4] and number[1]==number[3]:
		print("Palindromik sayıdır.")
	else:																					
		print("Palindromik sayı değildir.")	
def lenght():
	if len(number)!=5:
		print("Lütfen 5 basamaklı sayı giriniz !")
		enterNumber()
	else:
		testNumber()
enterNumber()


