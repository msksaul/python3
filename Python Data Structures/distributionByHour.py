name = input('Enter file: ')
if len(name) < 1 : name = 'mbox-short.txt'
fhandle = open(name)
list = dict()
for line in fhandle:
    if line.startswith('From '):
        line = line.split()
        line = line[5].split(':')
        list[line[0]] = list.get(line[0],0)+1
data = sorted([(k,v) for k,v in list.items()])
for k,v in data:
    print(k,v)
