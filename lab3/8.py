digits = []
while len(digits) != 5:
    x = int(input("Enter next digit = "))
    digits.append(x)
n = 0
count = 0
for i in digits:
    if i != digits[n]:
        count += 1
print(count)
