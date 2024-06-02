# class Vehicle:
#     def display():
#         print("I am a vehicle")
#     def Car(vehicle):
#         def m():
#             print("I am a car")
#     c=Car()
#     c.m()
#     c.display()
#             super().display()
    
    #Making an Bank account 

class BankAccount:
    def __init__(self,title,Balance,Account_no,):
        self.title=title
        self.Balance=Balance
        self.Account_no=Account_no
class Saving(BankAccount):
    def __init__(self,interestrate):
        self.interestrate=interestrate
        super().__init__("kishan",1500,2342)
class Current(BankAccount):
    def __init__(self,limit):
        self.limit=limit
        super().__("Sasank",2000,2342)

Ram=Saving(6)
print(Ram.title)
    



    


