n=int(input("Enter Times of  number:"))
ls=[]
sum=0
for i in range(n):
    ls.append(int(input()))
for i in range(n):
    sum+=ls[i]
print(sum)
