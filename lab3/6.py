# Дан список чисел.
# Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

first = [34, 48, -2, -1, -4, 6, 0, -81, 71, -91, 100, 13]
big = max(first)
small = min(first)

for a in first:
    if a == big:
        print(a, first.index(a))
    if a == small:
        print(a, first.index(a))
