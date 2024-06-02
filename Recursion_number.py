# def print_natural_number(l,r):
#     if(l>r):
#         return 
#     print(l)
#     print_natural_number(l+1,r)
#     return
# print_natural_number(1,15)



def table_two(l,r):
    if(l>r):
        return
    print(l) 
    print table_two(l+2,r)
    return
print table_two(1,20)
    