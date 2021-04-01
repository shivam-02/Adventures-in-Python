class aaa:
  x=10
  def sam(k,e):
    k.u=e

  def tom(k):
    print(k.u)

a=aaa()
b=aaa()
print(a.x)
print(b.x)
print(aaa.x)
a.sam(30)
b.sam(40)
a.tom()
b.tom()
#print(aaa.u) AttributeError: type object 'aaa' has no attribute 'u'
a.x=756 # Now it will create an attribute in a instance and a'x is no longer pointing to the old x int object.
print(a.x)
print(b.x) # but b is still pointing to old x int object.

aaa.x=444;
print(a.x)
print(b.x)