
n=int(input())
def sod(n):
    if(n<10):
        return n
    return n%10+sod(n//10)
def super_digit(n):
    if(n<10):
        return n
    return super_digit(sod(n))
print(super_digit(sod(n)))

