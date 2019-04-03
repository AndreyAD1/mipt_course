a = set('0123456789')
b = set('02468')
c = set('12345')
d = set('56789')

e = ((a-b) & (c-d)) | ((d - a) & (b - c))
print(e)
