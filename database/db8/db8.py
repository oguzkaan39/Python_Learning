#!usr/bin/env python3
#-*- coding:utf-8 -*-
#VERİ TABANI GÜVENLİĞİ
import sqlite3      
with sqlite3.connect('kullanicilar.sqlite3') as db8:
  im=db8.cursor()
  im.execute("CREATE TABLE IF NOT EXISTS kullanicilar (kullanici_adi, parola)")
  veriler = [
             ("ahmet123", "12345678"),
             ("mehmet321", "1231451"),
             ("selin1233", "12312031")]
  for i in veriler:
    im.execute("""INSERT INTO kullanicilar VALUES %s"""%(i,))
  db8.commit()
  kullanici_adi=input("Kullanıcı adınızı giriniz : ")
  parola=input("Parolanızı giriniz : ")
  im.execute("""SELECT * FROM kullanicilar WHERE kullanici_adi='%s' AND parola ='%s'"""%(kullanici_adi, parola))
  data=im.fetchone()
  if data:
    print("Programa hoş geldiniz".format(data[0]))
  else:
    print("Parola veya kullanici adı yanliş")