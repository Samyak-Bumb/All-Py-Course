myDictionary={
	"versatile": "Capable to do Many Things",
	"unknown": "Rapper",
	"marks": [1,2,6],
	"artist": {"unknown" : "Artist"},
	1 : 2
}

print(myDictionary.keys()) # Prints the Keys Only
print(list(myDictionary.keys())) # Prints the Keys in List Form Only
print(myDictionary.values()) # Prints the Values Only
print(myDictionary.items()) # Prints the All Keys & Values

# Updates the Dictionary
updateDictionary={
	"Word": "Hello world",
	"Slogan": "Code Never Lies",
	"unknown": "Artist",
}
myDictionary.update(updateDictionary)

print(myDictionary)

print(myDictionary.get("unknown")) # Gets The Value of the Key # Not Gives Any Error
# print(myDictionary["unknown"]) # Not Recommended + Sometimes Gives an Error
