#Write a python program for union in array

# def union_array(arr1,arr2):
#     return list(set(arr1+arr2))
# arr1=[1,2,3,4,1,2,5]
# arr2=[1,2,3,4,1,2]
# print(union_array(arr1,arr2))

#Second Method

def union_array(arr1,arr2):
    result=[]
    for i in arr1:
        if i not in result:
            result.append(i)
    for i in arr2:
            if i not in result:
                result.append(i)
    return result

arr1=[1,2,3,4,4,3,2,1223,454]
arr2=[1,2,3,9,8,7,1]
print(union_array(arr1,arr2))