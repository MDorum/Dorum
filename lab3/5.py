first = [34, 48, -2, -1, -4, 6, 0, -81, 71, -91, 100, 13]
#for a in range(1, 11):
    #first.append(a)
#print(first)
n = 0
for b in first:
    if n == len(first) - 1:
        continue
    elif first[n] < first[n + 1] and first[n + 1] > first[n + 2]:
        print(first[n + 1])
        n += 1
    else:
        n += 1