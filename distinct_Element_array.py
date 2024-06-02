#Write a function to find a distinct elements in an array

# def distinctElement(arr):
#     return list(set(arr))

# arr=[1,2,3,4,4,5,1,2,3,5,56]
# print(distinctElement(arr))



def distinct_element(arr):
    result=[]
    for i in arr:
        if i not in result:
            result.append(i)
    return result

arr=[1,2,3,4,5,1,2,3,4,56,7]
print(distinct_element(arr))


