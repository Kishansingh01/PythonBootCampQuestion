a=int(input("Enter a number a: "))
r=int(input("Enter a number r:"))
n=int(input("Enter a number n:"))
for i in range(1,n+1):
    GP=a*r**(i-1)
    print(GP)

# a = int(input("Enter the value of a: "))
# r = int(input("Enter the value of r: "))
# n = int(input("Enter the value of n: "))
 
# # 2. Loop for n terms
# for i in range(1,n+1):
#     t_n = a * r**(i-1)
#     print(t_n)