fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count=0

fhandle = open(fname)

for line in fhandle:
    line=line.rstrip()
    if line.startswith('From '):
        line=line.split()
        print(line[1])
        count=count+1

print("There were", count, "lines in the file with From as the first word")
