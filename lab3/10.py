digit = input("Enter all digits = ").split()
print(digit)
a = 0
b = 0
big = max(digit)
small = min(digit)
for i in digit:
    if big == i:
        a = digit.index(i)
    elif small == i:
        b = digit.index(i)

digit[a], digit[b] = digit[b], digit[a]
print(digit)