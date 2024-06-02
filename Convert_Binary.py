#Given a number convert it into binary form
n=int(input("Enter a number::"))
def binary(n):
    return bin(n)[2:]

print(binary(4))