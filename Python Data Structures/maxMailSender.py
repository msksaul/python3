# read through the mbox-short.txt and figure out who has sent the greatest
# number of mail messages
name = input('Enter file:' )
dictionary = dict()
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)
for line in handle:
    if line.startswith('From '):
        line = line.split()
        dictionary[line[1]] = dictionary.get(line[1],0)+1
maxcount = None
maxword = None
for word,count in dictionary.items():
    if maxcount is None or count > maxcount:
        maxword = word
        maxcount = count
print(maxword, maxcount)
