#Write a function to search string in an array

def search_string(arr,s):
    for i in range(len(arr)):
        if arr[i]==s:
            return i
    return -1
arr=["Ram",6,5,"I am kishan"]
print(search_string(arr,5))
