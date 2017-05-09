#!usr/bin/env python3
#-*- coding:utf-8 -*-
#fetchall() metodu ne iş yapar?
#fetchall() metodu ile verilerin alınması ve ekrana yazılması
import sqlite3, os
#Veritabanı dosyası, dosya adlı bir değişkene eşittir.
dosya = 'faturalar.sqlite3'
dosya_mevcut=os.path.exists(dosya)
db3=sqlite3.connect(dosya)
with sqlite3.connect('faturalar.sqlite3') as db3:
  im=db3.cursor()
  im.execute("CREATE TABLE IF NOT EXISTS faturalar ('fatura', 'miktar', 'son_ödeme_tarihi')")
  if not dosya_mevcut:
    im.execute("INSERT INTO faturalar VALUES ('Elektrik', 45, '10 Mayıs')")
  db3.commit()
  db3.commit()
  # '*' işareti tüm öğeler anlamına gelmektedir.
  im.execute("SELECT * FROM faturalar")
  #fetchall metodu tüm verileri aldı ve 'veriler' adlı değişkene atadı.
  veriler=im.fetchall()
  print(veriler)
  #Veritabanının ismini öğrenmek ;
  #Her veritabanında 'sqlite_master' tablosu vardır ve burada,
  #veritabanındaki tüm tabloların ismini yazar.
  def veritabanı_ismi():
    im.execute("SELECT name FROM sqlite_master")
    isim=im.fetchall()
    print(isim)
