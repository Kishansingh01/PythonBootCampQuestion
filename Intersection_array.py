#Calculate Intersection of two arrays
# def intersection(arr1,arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             if arr1[i]==arr2[j]:
#                 return arr1==arr2
                # print()
    #up code is wrong            




def intersection(arr1, arr2):
    return [i for i in arr1 if i in arr2]
arr1=[1,2,3,4,5]
arr2=[1,2,3,8,8]
print(intersection(arr1,arr2))
