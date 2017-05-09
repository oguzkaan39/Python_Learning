#!usr/bin/env python3
#-*- coding : utf-8 -*-
import sqlite3
with sqlite3.connect('deneme.sqlite') as deneme1:
  im=deneme1.cursor()
  im.execute("CREATE TABLE IF NOT EXISTS deneme1 (isim,soyisim,numara)")
  deneme1.commit()
  def veri_gir():
    global isim
    global soyisim
    global numara
    isim=input("İsim giriniz : ")
    soyisim=input("Soyisim giriniz : ")
    numara=input("Numara giriniz : ")
    im.execute("INSERT INTO deneme1 VALUES (?, ?, ?)",(isim,soyisim,numara))
    im.execute("SELECT numara FROM deneme1")
    numaralar=im.fetchone()
    sonuc=numaralar.count(numara)
    print(numaralar)
    deneme1.commit()
  veri_gir()
  
  


