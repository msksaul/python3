fname = input('Enter file name: ')
lines=0
average=0.0
add=0.0

try:
    fhand = open(fname)
except:
    print('File not found: ',fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        spinit = line.find(':')
        add=add+float(line[spinit+1:].strip())
        lines+=1

average=round(add/lines,15)

print('Average spam confidence:',average)
