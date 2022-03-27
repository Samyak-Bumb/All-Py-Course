number1=int(input("Enter number 1\n"))
number2=int(input("Enter number 2\n"))
number3=int(input("Enter number 3\n"))
number4=int(input("Enter number 4\n"))

# Checks Number1 and Number4
if(number1>number4):
	a1=number1
else:
	a1=number4

# Checks Number2 and Number3
if(number2>number3):
	a2=number2
else:
	a2=number3

if(a1>a2):
	print(str(a1) + " is the Greatest Number!")
else:
	print(str(a2) + " is the Greatest Number!")
