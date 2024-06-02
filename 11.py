a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
if(a+b>c and b+c>a and c+a>b):
    print("The three side are the triangle")
else:
    print("The three sides are not triangle")