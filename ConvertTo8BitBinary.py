d = int(input('Enter a decimal integer from 0 to 255: '))
b = str()
for exp in [7, 6, 5, 4, 3, 2, 1, 0]:
    if d >= 2 ** exp:
        d -= 2 ** exp
        b += '1'
    else:
        b += '0'
print(b)
