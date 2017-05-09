#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sqlite3
with sqlite3.connect('personel.sqlite3') as db2:
  im=db2.cursor()
  #Veriler dizisinin oluşturulması
  veriler=[('Oguzkaan', 'Gündüz', 'Lüleburagaz'),
           ('Serap', 'Duran', 'Balıkesir'),
           ('Atilla', 'Gündüz', 'Antalya'),
           ('Hüseyin', 'Duran', 'Balıkesir')]
  def tablo_yap():
    im.execute("CREATE TABLE IF NOT EXISTS personel (isim, soyisim, memleket)")
  for veri in veriler:
    #Dizi içindeki elemanları veritabanına kaydetmek
    im.execute("INSERT INTO personel VALUES (?, ?, ?)",veri)
  tablo_yap()
  db2.commit()