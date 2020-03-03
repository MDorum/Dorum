a = []
i = 1
while i != 10:
    i += 1
    x = input("Enter value = ")
    a.append(x)
print(a)
n = 0
for l in a:
    #print(print(a[n]))
    #n += 2
    try:
        print(print(a[n]))
        n += 2
    except IndexError:
        print("Out of range")

