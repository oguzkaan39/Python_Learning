#!usr/bin/env python3
#-*- coding:utf-8 -*-
#Veri Süzme
import sqlite3
with sqlite3.connect('kitaplar.sqlite') as db6:
  im=db6.cursor()
  #im.execute("SELECT * FROM kitaplar")
  #Tablonun ismini öğrenmek
  im.execute("SELECT name FROM sqlite_master")
  #Sütun başlıklarını öğrenmek
  #im.execute("SELECT sql FROM sqlite_master")
  #isim=im.fetchall()
  #print(isim)
  #Yazar = Fırat Özgül'ü Filtrelemek
  im.execute("SELECT * FROM kitaplar WHERE Yazar='Fırat Özgül'")
  #Seçilen veriyi fetchall() metodu ile alma
  #yazar=im.fetchall()
  #Aldığımız veriyi ekrana yazdırma
  #print(yazar)
  #For Döngüsü ile veriyi ekrana yazdırma
  for s in im:
    print(s)
  #Yıldızlı ifade ile veriyi ekrana yazdırna
  print(*im)