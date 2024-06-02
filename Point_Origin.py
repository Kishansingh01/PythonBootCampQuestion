# import math
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def distance(self):
#         return math.sqrt(self.x**2+self.y**2)
# coor=Point(4,5)
# print(coor.distance())

import math    
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self):
        return math.sqrt(self.x**2+self.y**2) 
coor=Point(4,6)
print(coor.distance())

    
    

        
        