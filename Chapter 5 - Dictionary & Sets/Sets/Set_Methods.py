a=set()

print(type(a))

# Adding Values to any Empty Set
a.add(1)
a.add(6)
a.add(9)
 # If a Value is Added then also Set Does't Change
a.add(6)
a.add(9)

# a.add([6,9,69]) # List is Not Allowed In Sets Because its UnHashable (Gives an Error)

# a.add({6,9,69}) # Dictionary is Not Allowed In Sets Because its UnHashable (Gives an Error)

a.add((6,9,69)) # Tuple is Allowed In Sets

print(a)

print(len(a)) # Prints Length of the Set

# Removes an Item/Item's
a.remove((6,9,69)) # Removes the Tuple Items form Set
a.remove(1) # Removes 1 form Set

print((a)) # Prints Length of the Set

print(a.pop()) # Remove and return an Arbitrary Set Element
