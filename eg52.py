a="        abcd       "

b=a.lstrip()
c=a.rstrip()
d=a.strip()

print(a)
print(b)
print(c)
print(d)

e="\n       abcd     \n"
print(e.strip())
# strip not only remove white space but also remove newline(\n) character
