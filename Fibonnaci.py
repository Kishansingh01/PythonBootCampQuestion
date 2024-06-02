n=int(input())
class Solution:
    def __init__(self):
        pass
    def fib(self,n):
        if(n<=1):
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
kishan=Solution()
print(kishan.fib(n))