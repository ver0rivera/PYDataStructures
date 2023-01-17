
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    total += float(line[20:-1].strip())
    count += 1
   
    
print("Average spam confidence:", (total/count))