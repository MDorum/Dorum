digits = []
while len(digits) != 5:
    x = int(input("Enter new digit = "))
    digits.append(x)
print("It is new list =", digits)
x1 = int(input("Which index you want to delete = "))
for i in digits:
    digits[x1 + 1], digits[x1] = digits[x1], digits[x1 + 1] #нужно придумать алгоритм перебора
print("List after changing =", digits)
digits.pop()
print("Result after deleting =", digits)
