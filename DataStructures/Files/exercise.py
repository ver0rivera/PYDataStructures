# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

fname = input('the name')
files = open(fname, 'r')
reading = files.read()
upeerad = reading.upper()
print(upeerad.rstrip())
files.close
