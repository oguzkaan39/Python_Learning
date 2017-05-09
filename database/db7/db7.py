#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Bu bir pratik yapma dosyası olup db6.py dosyası ile
#hemen hemen aynıdır!
import sqlite3
with sqlite3.connect('kitaplar.sqlite') as db7:
  im=db7.cursor()
  im.execute("SELECT * FROM kitaplar WHERE Yazar='Fırat Özgül'")
  #print(*im)
  for s in im:
    print(s)