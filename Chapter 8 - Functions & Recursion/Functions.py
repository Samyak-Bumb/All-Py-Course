def percent(marks):
	return((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

marks=[95,83,69,61]

percentage1=percent(marks)

marks=[59,38,69,16]

percentage2=percent(marks)

print(percentage1,percentage2)
