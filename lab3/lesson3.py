# # Ввести число и возвести его в куб, проверить на то, что это число.
#
# x = input("Enter value = ")
# try:
#     x = int(x)
#     print(x**3)
# except:
#     print("It's not a digit.")
#

# # Получить на ввод количество рублей и копеек и вывести в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки (*)
#
# # 1 рубль копейка
# # 2 - 4 рубля копейки
# # 5 - 20 рублей копеек
# # 21 - рубль копейка
# # 22 - 24 рубля копейки
# # 25 - 30 рублей копеек
# # 31 - рубль 31 копейка
# # 32 - 34 рубля копейки
# # 35 - 40 рублей копеек
#
# a, b = map(int, input("Че там = ").split())
# if a % 10 == 1:
#     print(a, "рубль")
# elif a % 10 == 0:
#     print(a, "рублей")
# elif a % 10 in range(2, 5):
#     print(a, "рубля")
# elif a % 10 in range(5, 21):
#     print(a, "рублей")
#
# if b % 10 == 1:
#     print(b, "копейка")
# elif b % 10 == 0:
#     print(b, "копеек")
# elif b % 10 in range(2, 5):
#     print(b, "копейки")
# elif b % 10 in range(5, 21):
#     print(b, "копеек")


# Поле шахматной доски определяется парой натуральных чисел,
# каждое из которых не превосходит 8: первое число — номер вертикали (при счете слева направо),
# второе — номер горизонтали (при счете снизу вверх).
# Даны натуральные числа a, b, c, d, каждое из которых не превосходит 8. (**)

# x, y= map(int, input("Gde stoit figuta = ").split())
#
# for i in range(1, 9):
#     for j in range(1, 9):
#         #print(i, j, end="  ")
#         if x == i and y == j:
#             print("Фигура находится в точке =", i, j)
#
#             # print("Фигура угрожает полю =", i + 2, j + 1)
#             # print("Фигура угрожает полю =", i + 2, j - 1)
#             # print("Фигура угрожает полю =", i - 2, j + 1)
#             # print("Фигура угрожает полю =", i - 2, j - 1)

a = input("Введите текущую координату фигуры(вертикаль): ")
b = input("Введите текущую координату фигуры(горизонталь): ")
c = input("Введите координату для хода(вертикаль): ")
d = input("Введите координату для хода(горизонталь): ")
# Условие
if (a==c) and (b==c):
    print("Фигура может сделать ход")
else:
    print("Фигура НЕ может сделать ход")