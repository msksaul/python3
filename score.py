sc = input('Enter score: ')
score = float(sc)
if score > 1.0:
    print('Score out of range')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
