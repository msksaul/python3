def computepay(hours,rate):
    if h <= 40 :
        return hours*rate
    else:
        return 40*rate + (hours-40)*rate*1.5

hrs = input('Enter hours: ')
h = float(hrs)
rateph = input('Enter rate: ')
r = float(rateph)

pay = computepay(h,r)
print('Pay', pay)
