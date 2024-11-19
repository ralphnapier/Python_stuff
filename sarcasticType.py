#This code takes any string for "sentence' and converts it to sarcastic type style, LiKe tHiS 5/15/24

sentence = 'one more exercise, then you can relax.'
result = ''
caps = True

for _ in sentence:

    if caps:
        result += _.upper()
        caps = False
    else:
        result += _.lower()
        caps = True
print(result)
