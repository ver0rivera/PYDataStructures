# Often we want to find the “interesting lines”
#  and then parse the line to find some interesting part of the line.
print('EXAMPLE WITH FILES')
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('pero'):
        continue
    words = line.split()
    print(words[2])
