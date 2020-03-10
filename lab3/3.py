#first = [-1, -2, 3, 4, -1] #список
first = []
while len(first) != 5:
    digit = int(input("Enter the digit = "))
    first.append(digit)
n = 0
for d in first: #перебирает все числа в списке
    if n == len(first) - 1: #условие, чтобы индекс не выходил за пределы размера списка
        continue
    elif first[n] >= 0 and first[n + 1] >= 0 or first[n] < 0 and first[n + 1] < 0: #блок условия
        print(first[n], first[n + 1], sep=" and ")
        n += 1
    else:
        n += 1