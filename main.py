import math

# Welcome Screen

print("\t Hello Welcome to Calk!")
print("\t Read my doc page on Github  \n https://github.com/Nivin389/Calk#readme \n\tDont Fork me ! Give it a Star!")

# 3 Var 2 int one str

a = int(input("Enter Number A :"))
b = int(input("Enter Number B :"))
Op = input("Enter Operation :")


# If Functions to run the calk

if Op == '+' :
    print("The Answer is :", a+b)
    print("Thank you For Using me ! Please Give it a Star ")

if Op == '-':
    print("The Answer is :", a-b)
    print("Thank you For Using me ! Please Give it a Star ")

if Op =='*':
    print("The Answer is :", a*b)
    print("Thank you For Using me ! Please Give it a Star ")

if Op == '/':
    print("The Answer is :", a/b)
    print("Thank you For Using me ! Please Give it a Star ")

if Op == '%':
    print("The Answer is :", a%b)
    print("Thank you For Using me ! Please Give it a Star ")

if Op == '**':
    print("The Answer is :" , a**b)
    print("Thank you For Using me ! Please Give it a Star ")

if Op == '//':
    print("The Answer is :" , a//b)
    print("Thank you For Using me ! Please Give it a Star ")

# Error catch

if a == 0 and b == 0:
    print("Error! 2 inputs can't be 0")

if Op.isnumeric():
    print("\tError!\n Cant Use Operator with a numeric Value" , [Op])