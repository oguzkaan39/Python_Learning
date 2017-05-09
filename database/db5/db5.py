#!usr/bin/env python3
#-*- coding:utf-8 -*-
#fetchmany() metodu kullanılması
import sqlite3
with sqlite3.connect('kitaplar.sqlite') as db5:
  im=db5.cursor()
  im.execute("SELECT * FROM kitaplar")
  #3 adet veri seçip bir degiskene atamak.
  secilen_degerler=im.fetchmany(3)
  print("----------------------")
  #For döngüsünü direkt olarak imleç üzerine koyabiliriz.
  print(secilen_degerler)
  for veri in im:
    print(veri)