# to perform simple calculator 

print("to choose a operation:")
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")

opt=int(input("enter choice(1-4):"))

num1=float(input("enter first no:"))
num2=float(input("enter second no:"))
# to perform calculation
if opt == 1:
    result=num1+num2
elif opt == 2:
    result=num1-num2
elif opt == 3:
    result=num1*num2
elif opt == 4:
    result=num1/num2

print(result)
