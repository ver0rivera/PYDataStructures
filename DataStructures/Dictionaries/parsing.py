import string
# try with romeo-full.txt


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# Since the Python split function looks for spaces and treats
# words as tokens sep- arated by spaces,
# we would treat the words “soft!” and “soft” as different
# words and create a separate dictionary entry for each word.

# We can solve both these problems by using the string
# methods lower, punctuation, and translate.

# We use translate to remove all punctuation and
# lower to force the line to lower- case.
