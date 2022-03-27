number=int(input("Enter a number\n"))

factorial=1

for i in range(1, number + 1):
	factorial=factorial * i

print(f"The factor of this number is\n{factorial}")
