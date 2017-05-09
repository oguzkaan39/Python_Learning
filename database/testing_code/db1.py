#!usr/bin/env python3
#-*- coding:utf-8 -*-
import sqlite3
#Veritabanına bağlanmak
with sqlite3.connect('veritabani.sqlite') as db1:
  #İmlecin oluşturulması
  imlec=db1.cursor()
  def tablo_yap():
    #Tablo oluşturulması
    imlec.execute("CREATE TABLE IF NOT EXISTS kisiler (isim,soyisim,numara)")
    #Yapılan değişikliklerin kaydedilmesi
    db1.commit()
  def veri_gir():
    global ad
    global soyad
    global numaraniz
    ad=input("İsminizi giriniz : ")
    soyad=input("Soyadınızı giriniz : ")
    numaraniz=int(input("Numaranızı giriniz : "))
    #Dışarıdan girilen değerlerin tabloya kaydedilmesi
    imlec.execute("INSERT INTO kisiler VALUES (?,?,?)",(ad,soyad,numaraniz))
    #Yapılan değişikliklerin kaydedilmesi
    db1.commit()
  def veri_sec():
    global numaralar
    #numaralar sütunundaki verilerin seçilmesi
    imlec.execute("SELECT numara FROM kisiler WHERE numara")
    #Secilen verilerin numaralar değişkenine atanması
    numaralar=imlec.fetchall()
    #Verilerin ekrana yazılması
    print(numaralar)
  def kontrol():
    numaraa=input("Numara giriniz :")
    #Girilen numara numaralar'ın içindeyse;
    if numaraa in numaralar:
     print("numara burda var")
    #Girilen numara numaralar'ın içinde değilse;
    else:
     print("Numara burda yok")
  #Şu an sadece numara sütunundaki verileri seçtik.
  #Kontrol fonksiyonu ile de dışarıdan girilen numaranın,
  #seçtiğimiz verilerin içinde var mı yok mu onun kontrolünü yaptık.
  tablo_yap()
  veri_sec()
  kontrol()
  