#Check larger of the three number
a=int(input("Enter a number a:"))
b=int(input("Enter a number b:"))
c=int(input("Enter a number c:"))
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
elif(c>a and c>b):
    print("c is greater")
elif(a==b and b==c):
    print("All are equal")
elif(a==b and b>c):
    print("a and b are equal")
elif(b==c and b>c):
    print("b and c are greater")
elif(a==c and a>b):
    print("a and c is greater")


    
    



