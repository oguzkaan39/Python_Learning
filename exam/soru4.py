#!usr/env/bin python
#-*- coding:utf-8 -*-
#------------------------------------------SORU---------------------------------------------
#Aşağıdaki seride x sayısı diğer sayıların ortalamasıdır.
# 'x' sayısını bulunuz ve Aşağıda yorum satırıyla belirtilen dizideki,
# x'in yerine koyunuz ve ekrana yazdırınız.
#Daha sonra dizinin yeni halini elemanlarının küçükten büyüğe sıralanmış şekilde yazdırınız.
#-------------------------------------------------------------------------------------------
#seri=[3,4,5,x,15,25,36,45,57,7]
seri=[3,4,5,15,25,36,45,57,7]
# x=sayıların ortalaması
toplam=0
for i in range(0,9):
	toplam=toplam+seri[i]
x=toplam/9
seri.insert(3,x)
print("Listenin sıralama bozulmadanki hali;\n",seri)
print("Bulunan x sayısı =",x)
seri.sort()
print("Listenin küçükten büyüğe sıralanmış hali;\n",seri)