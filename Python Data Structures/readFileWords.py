fname = input('Enter file name: ')
wordlist=list()
temp=list()
count=0

def removeDupLine(line):
    line=line.split()
    s = []
    for i in line:
        if i not in s:
            s.append(i)
    return s

try:
    fhand = open(fname)
except:
    print('File not found: ',fname)
    quit()

for line in fhand:
    line = removeDupLine(line)
    for i in range(len(line)):
        word = line[i]
        if len(wordlist) == 0:
            wordlist.append(word)
        else:
            for i in range(len(wordlist)):
                count=count+1
                if word == wordlist[i]:
                    break
                else:
                    if count == len(wordlist):
                        temp.append(word)
            count=0
    wordlist=wordlist+temp
    temp=list()

wordlist.sort()
print(wordlist)
