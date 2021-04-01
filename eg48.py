import array

a=array.array('i')
a.append(10)
a.append(30)
a.append(40)

print(a)

for x in a:print(x)

print(a[0])
print(len(a))
print(a.itemsize)