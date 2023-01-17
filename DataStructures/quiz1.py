

text = "X-DSPAM-Confidence:    0.8475"
finder = text.find('0')
# print(finder)

findEnd = text.find('', finder)
# print(findEnd)

final = text[finder:findEnd+6]
print(float(final))
