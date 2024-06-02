#Calculate sum of each column in 2D array

def column_summation(arr1):
    return [sum(col)for col in zip(*arr1)]
arr1=[[1,2,3],[4,5,6],[6,7,8]]
print(column_summation(arr1))


#   *Zip function is used to transpose an array