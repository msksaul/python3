text = 'X-DSPAM-Confidence:    0.8475';
spinit = text.find(':')
num = float(text[spinit+1:].strip())
print(num)
