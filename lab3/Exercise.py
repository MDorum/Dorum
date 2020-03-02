#name = ['Ivanov', 'Petrov']
#goods = ['Paper', 'Pens', 'Marker', 'Envelope']
#count = [10, 5, 3, 7, 20, 5]
name = []
goods = []
count = []
dic = dict(zip(goods, count))
i = 0
while i != 6:
    i += 1
    a = str(input('Кто покупает? '))
    if a not in name:
       name.append(a)
    b = str(input('Что было куплено? '))
    if b not in goods:
       goods.append(b)
    else:
        for i in dic:
            if b == i:
                dic.update()


    c = int(input("В каком количестве была совершена покупка? "))
    count.append(c)


print(name)
print(goods)
print(count)
print(dic)


