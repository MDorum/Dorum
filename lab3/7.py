group = []
while len(group) != 5:
    height = int(input("Enter person's height = "))
    if height > 200:
        print("Height can't be more than 200 cm.")
    else:
        group.append(height)
peter_height = int(input("Enter Peter's height = "))
group.append(peter_height)
group.sort()
group.reverse()
pos = 0
for i in group:
   if i >= peter_height:
       pos += 1
print(group)
print("Peter should stay by the number", pos)