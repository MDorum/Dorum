#name = []
goods = []
count = []
i = 0
while i != 3:
    i += 1
    #x = str(input("Enter the name of the customer = "))
    #name.append(x)
    y = str(input("What does costumer buy = "))
    if y not in goods:
        goods.append(y)
    elif y in goods:

    z = int(input("How many = "))
    count.append(z)
first = dict(zip(goods, count))
for l in first:
    print(l, first[l])


#second = dict(zip(name, first))
#print(second)


#Ivanov paper 10
#Petrov pens 5
#Ivanov marker 3
#Ivanov paper 7
#Petrov envelope 20
#Ivanov envelope 5
