digit = input("Enter all digits = ").split()
print(digit)
n = 1
for i in digit:
    if n < len(digit):
        digit[n - 1], digit[n] = digit[n], digit[n - 1]
        n += 2
print(" ".join(digit))
