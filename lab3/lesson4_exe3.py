first = (0, 1, 2, 3)
print("Len of the first is", len(first))
second = ["A", "B", "C", "D", "E"]
print("Len of the second is", len(second))
result = 0
def slovar():
    global second
    global result
    if len(first) != len(second):
        a = len(first) - len(second)
        print("Check the len", a)
        if a < 0:
            a *= -1
            print("Smena znaka", a)
        for i in range(0, a):
            second.pop()
    result = dict(zip(first, second))

slovar()
print(first)
print(second)
print("Result of the exe:", result)