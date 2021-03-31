a=10
b=20
z=a+b
print("Total of %d and %d is %d"%(a,b,z))
print("Total of {} and {} is {}".format(a,b,z))
print("Total of {} and {} is {}".format(z,b,a))
print("Total of {2} and {1} is {0}".format(z,b,a))
print("Total of {num1} and {num2} is {sum}".format(sum=z,num2=b,num1=a))
print(f"Total of {a} and {b} is {z}")
print(f"Total of {a} and {b} is {a+b}")