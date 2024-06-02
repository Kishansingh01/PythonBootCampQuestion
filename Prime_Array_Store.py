#Store first n prime number in an array

# n=int(input("Enter number of prime number you want::"))
# def prime(n):
#     for i in range(2,n+1):
#         if (n<=1):
#             print("Not a prime number")
#         if(n%i!=0):
#             print(i)

#UP code is not right


def prime_number(n):
    primes=[]
    i=2
    while len(primes)<n:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            primes.append(i)
        i+=1
    return primes

print(prime_number(10))


    
    
