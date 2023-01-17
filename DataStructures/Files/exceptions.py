
fname = input('file.txt')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Test:'):
        count = count + 1
print('There were', count, 'test lines in', fname)
