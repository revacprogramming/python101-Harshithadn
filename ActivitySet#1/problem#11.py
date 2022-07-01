# Tuples

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
file1 = open(name)
dct = dict()
for line in file1:
    if line.startswith("From "): 
        lst = line.split()
        num = lst[5]
        time = num.split(":")
        dct[time[0]] = dct.get(time[0],0) + 1
ftime = sorted(dct.items())
for (k,v) in ftime:
    print(k,v)