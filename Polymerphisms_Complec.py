class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,b):
        return Complex(self.real+b.real,self.imaginary+b.imaginary) 
kishan=Complex(2,3)
sasank=Complex(4,6)
Ram=kishan+sasank
print(Ram.real,Ram.imaginary)e