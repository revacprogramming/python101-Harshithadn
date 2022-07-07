fhandle = open('mbox-short.txt')
count = 0
for line in fhandle:
    if line.startswith('From'):
        list = line.strip()
        list = line.split()
        if list[0] == 'From:':
            continue
        print(list[1])
        count = count + 1
print('There were',count,'lines in the file with From as the first word')