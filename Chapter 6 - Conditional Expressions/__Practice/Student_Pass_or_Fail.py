subMarks1=int(input("Enter 1st Subject Marks\n"))
subMarks2=int(input("Enter 2nd Subject Marks\n"))
subMarks3=int(input("Enter 3rd Subject Marks\n"))

if(subMarks1<33 or subMarks2<33 or subMarks3<33):
	print("Sorry! You'r \"Failed\"")

elif(subMarks1+subMarks2+subMarks3)/3 < 40:
	print("You are fail due to total Percentage less than 40")
else:
	print("Congratulations! You'r \"Passed\"")
