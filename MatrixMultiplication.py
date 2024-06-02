#Program for matrix multiplication                                                                                                                                                       n1=int(input("Row size of first array "))
m1=int(input("Column size of first array "))
n2=int(input("Row size of second array "))
m2=int(input("Column size of second array "))
n1=int(input("Row size of second array"))
arr1=[]
arr2=[]

if(m1!=n2):
    print("Matrix multiplication is not possible ")
    exit(0)

print("Enter the elements of first array ")
for i in range(n1):
    row1=[]
    for j in range(m1):
        row1.append(int(input()))
    arr1.append(row1)

print("Enter the elements of second array ")
for i in range(n2):
    row2=[]
    for j in range(m2):
        row2.append(int(input()))
    arr2.append(row2)

arr3=[]
for i in range(n1):
    row3=[]
    for j in range(m2):
        sum=0
        for k in range(n2):
            sum+=arr1[i][k]*arr2[k][j]
        row3.append(sum)
    arr3.append(row3)

for i in range(n1):
    for j in range(m2):
        print(arr3[i][j],end=" ")
    print("")