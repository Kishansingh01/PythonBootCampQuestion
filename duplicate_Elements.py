#Write a python program to print duplicate of an array

def duplicate_array(arr):
    for i in arr:
        if arr.count(i)>1:
            return i
    return "NO Duplicate"
arr=[1,2,3,4,5,1,2,3,6]
print(duplicate_array(arr))

#Note=Up codind will print number of times 
#duplicate u have taken



#Here u have to understand difference between 
#print and return
        

            
