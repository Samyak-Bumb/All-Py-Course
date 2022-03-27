number=int(input("Enter number\n"))
prime=True

for i in range(2, number):
    if (number % i == 0):
        prime = False
        break

if prime:  # Note: Don't give Tab
    print("Yess is Prime")
else:
    print("Not Prime")
