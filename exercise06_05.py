#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
pos_init = text.find('0')
#print(pos_init)
pos_fin = text.find('5')
#print(pos_fin)
num = float(text[23:])
print(num)