#Calculate sum of each row in 2D array

def row_summation(arr1):
    return [sum(row) for row in arr1]

arr1=[[1,2,3],[2,3,4],[4,5,6]]
print(row_summation(arr1))