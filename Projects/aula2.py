print("Data detection program.")
name=input("Enter your name: ")
print("Welcome, ", name,". Now, the good old calculator thing.", sep="")
num1=input("Enter the first number: ")
num2=input("Enter the second number: ")

castNum1 = int(num1) #casting the input to int
if(type(castNum1) == float):
    print("Are you stupid? That's not an integer.")
    exit()
else:
    castNum2 = int(num2) #casting the input to int
if(type(castNum2) == float):
        print("Are you stupid? That's not an integer.")
else:
     result = castNum1 + castNum2
#note: it could be casted with "print("The sum of the numbers is: ", int(num1) + int(num2), sep="")
print("The sum of the numbers is: ", result, sep="")
print("Now, we do it again with float numbers.")
floatNum1=input("Enter the first float number: ")
floatNum2=input("Enter the second float number: ")
result = float(floatNum1) + float(floatNum2)
print("The sum of the numbers is: ", result, sep="")



  
