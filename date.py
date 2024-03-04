# -*- coding: utf-8 -*-
from datetime import date

birthyear = int(2022)
birthmonth = int(8)
birthday = int(27)

daynow = date.today().strftime('%Y-%m-%d').split('-')
age_y = int(daynow[0])-(birthyear)
age_m = int(daynow[1])-(birthmonth)
age_d = int(daynow[2])-(birthday)

print ('วันปัจจุบัน '+date.today().strftime('%d-%m-%Y'))
print ('วันเกิด %d - %d - %d'%(birthday,birthmonth,birthyear))
print ('===============================')
print ('อายุของคุณ %d ปี %d เดือน %d วัน' %( age_y,age_m,age_d))