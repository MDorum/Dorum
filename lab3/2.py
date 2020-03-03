digit = []
new_digit = []
while len(digit) != 10:
    x = input("Enter digit = ")
    if type(x) is str:
        try:
            x = int(x)
            #print("You have entered digit. Congratulations!")
            digit.append(x)
        except:
            print("This is not digit. Try again.")
n = 0
for i in digit:
        if n + 1 == len(digit):
            continue
        elif digit[n + 1] > digit[n]:
            new_digit.append(digit[n + 1])
            n += 1
        else:
            n += 1
print(new_digit)