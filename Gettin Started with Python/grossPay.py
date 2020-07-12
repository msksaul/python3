hrs = input('Enter hours: ')
ratePerHour  = input('Enter rate: ')
h = float(hrs)
r = float(ratePerHour)
pay = 0.0
if h <= 40 :
    pay = h*r
else:
    pay = 40*r + (h-40)*r*1.5
print(str(pay))
