#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sqlite3
with sqlite3.connect('veriler2.sqlite') as db9:
  im=db9.cursor()
  
  def tablo_yap():
    im.execute("CREATE TABLE IF NOT EXISTS kisiler(isim, soyisim,numara)")
    db9.commit()
  def ekle():
    global isim
    global soyisim
    global numara
    isim=input("İsim giriniz : ")
    soyisim=input("Soyisim giriniz : ")
    numara=int(input("Numara giriniz : "))
    #Girilen numara kullanılmış mı?
    check()
    db9.commit()
  def sil():
    sil=int(input("Silinecek numara giriniz : "))
    im.execute("DELETE FROM kisiler WHERE numara=(?)",(sil))
  def check():
    im.execute("SELECT numara FROM kisiler ")
    numaralar=im.fetchall()
    if numaralar.count(numara) >=1:
      im.execute("INSERT INTO kisiler VALUES (?, ?, ?)",(isim,soyisim,numara))
    else:
      print("BAŞARILI")
    
      
  def secim():
    print("Veri Girmek için (1) tuşlayınız ")
    print("Girilmiş veriyi silmek için (2) tuşlayınız ")
    secim=int(input("Hangi işlemi yapmak istiyorsunuz ?(1/2):"))
    if secim==1:
      ekle()
    if secim==2:
      sil()
  tablo_yap()
  secim()
  #ekle()