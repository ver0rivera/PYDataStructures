# To write a file, you have to open it with mode “w” as a second parameter:

fout = open('output.txt', 'w')
print(fout)

# If the file doesn’t exist, a new one is created
# si el documento ya existe, lo reescribe
line1 = "hola pinche putita\n"
# añade la linea anterior al nuevo documento
fout.write(line1)

line2 = "que pedo raza\n"
fout.write(line2)

# When you are done writing, you have to close the file to make sure
# that the last
# bit of data is physically written to the disk so it will
# not be lost if the power goes
# off.

fout.close
