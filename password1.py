#!usr/bin/python
#-*- coding : utf-8 -*-
#Kullanıcıdan bir parola isteyin daha sonra belirlediği parola ile sisteme giriş yapmasını sağlayın
#Parola yanlışsa tekrar giriş hakkı tanıyın. 
def createPassword():
	global parola1,parola2
	parola1=int(input("Oluşturulacak parolanızı giriniz : "))
	parola2=int(input("Oluşturduğunuz parolayı doğrulamak için tekrar giriniz : "))
	verifyPassword()
def verifyPassword():
	global parola3
	if parola1==parola2:
		parola3=parola1 and parola2
		print("Parolanız başarılı bir şekilde belirlendi.")
		choice()
	else:
		print("Parolalar eşleşmedi!")
		print("Yeniden parola belirleyiniz !")
		createPassword()
def choice():
	secim=int(input("Giriş yapmak için 1, Çıkış için 0 tuşlayınız"))
	if secim==1:
		login()
	elif secim==0:
		print("Programdan çıkış yaptınız !")
	else:
		print("Yanlış tuşlama yaptınız !")
		choice()
def login():
	x=int(input("Giriş yapmak için parolanızı giriniz : "))
	if x==parola3:
		print("Sisteme başarılı bir şekilde giriş yaptınız.")
	else:
		print("Parolanız Hatalı! Tekrar giriniz ")
		login()
	
createPassword()

