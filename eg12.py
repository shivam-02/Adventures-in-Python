x=dict()

x={1:"shivam",2:"sugandhi"}
print(x)

print(x.get(1,0))
print(x.get(4,2))

for a,b in x.items():
  print(a,b)