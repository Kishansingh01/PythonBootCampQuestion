# n=int(input("Enter rows:"))
# m=int(input("Enter the columns"))
# for row in range(n):
#     for column in range(n):
#         if(row==)
#         print("*",end=" ")
#     print()


for row in range(7):
    for col in range(5):
        if(col==0 and col==4)and (row!=0 and row!=6) or(row==0 or row==6)and (col>0 and col<4):
            print("*",end="")
        else:
            print(end=" ")
    print()