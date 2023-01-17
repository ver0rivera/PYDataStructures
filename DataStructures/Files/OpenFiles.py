# For open a file
example = open('file.txt')
print(example)


# for count a number of lines in a file
count = 0
for line in example:
    count = count+1
print('Line Count:', count)

# If you know the file is relatively small compared to the size of your main memory,
# you can read the whole file into one string using the read method on the file handle.
files = open('file.txt')
reading = files.read()
print(len(reading))
print(reading[:20])

# searching througth data in a file
theFile = open('file.txt')
counter = 0
for line in theFile:
    if line.startswith('Test:'):
        print(line)

# the same but without the space between the lines
testing = open('file.txt')
for line in testing:
    line = line.rstrip()
    if line.startswith('Test:'):
        print(line)

# ahora alreves, imprime todas las lineas que no inicien con 'Test:'

tester = open('file.txt')
for line in tester:
    line = line.rstrip()
# Skip 'uninteresting lines'
    if not line.startswith('Test:'):
        continue
# Process our 'interesting' line
print(line)

#te va a imprimir las lineas que inicien con la palabra deseada
oper = open('file.txt')
for line in oper:
    line = line.rstrip()
    if line.find('pero') == -1:
        continue
    print(line)
