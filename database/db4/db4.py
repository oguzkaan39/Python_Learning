#!usr/bin/env python3
#-*- coding:utf-8 -*-
#fetchone() metodu ne iş yapar?
#fetchone() metodu veritabanından verilerin tek tek alınabilmesine izin verir.
import sqlite3
with sqlite3.connect('kitaplar.sqlite') as db4:
  im=db4.cursor()
  im.execute("SELECT * FROM kitaplar")
  #fetchone() metodunun kullanılması
  kitap=im.fetchone()
  #Alınan değerin ekrana yazdırılması
  print(kitap)