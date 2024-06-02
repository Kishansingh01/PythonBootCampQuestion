#To check whether a mumber is prime or not

n=int(input("Enter a number n:"))
if(n==1):
    print("1 is nothing")

for i in range(2,n+1):
    if (n%i==0):
        print("n is a prime number")
        break
    else:
        print("n is not a prime number")
        break

