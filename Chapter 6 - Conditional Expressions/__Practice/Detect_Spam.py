txt=input("Enter the Text: ")

if("Make a lot of Money" in txt):
	spam=True
elif("Buy Now" in txt):
	spam=True
elif("Watch this" in txt):
	spam=True
elif("Click this" in txt):
	spam=True
elif("Subscribe" in txt):
	spam=True

else:
	spam=False

if(spam):
	print("Don't Spam! Motherfucker🤬!!!")
else:
	print("Good! There is no Spam")
