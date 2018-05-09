import datetime

dt = dir(datetime)
print(dt)

dt = datetime.date.today()
print(dt)

dt = datetime.date(2017,10,15)
print(dt)

a = datetime.time(21,30,56)
print(a)

a = datetime.datetime(2050,12,31)
print(a)

a = datetime.datetime(2050,12,31,23,50,57)
print(a)

a = datetime.datetime.now()
print(a)

print(datetime.MINYEAR)
print(datetime.MAXYEAR)


