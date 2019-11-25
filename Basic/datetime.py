#!/usr/bin/python
import time;  # This is required to include time module.


ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks) #Number of ticks since 12:00am, January 1, 1970: 1555928020.4221191

#Getting current time
localtime = time.localtime(time.time())
print ("Local current time :", localtime) #Local current time : time.struct_time(tm_year=2019, tm_mon=4, tm_mday=22, tm_hour=17, tm_min=8, tm_sec=53, tm_wday=0, tm_yday=112, tm_isdst=0)

#Getting formatted time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime) #Local current time : Mon Apr 22 17:13:40 2019

#Getting calendar for a month
import calendar;
cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)

import datetime

x=	datetime.datetime.now()

print("Year",x.year)
print(x.strftime("%A"))