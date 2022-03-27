myDictionary={
	"sangank": "Computer",
	"dimag": "Brain",
	"ekonSttar": "69"
}

print("Options are here\n", myDictionary.keys())

a=input("Enter the Word\n")

# print("Meaning: ", myDictionary[a]) # Gives an Error

print("Meaning: ", myDictionary.get(a))
