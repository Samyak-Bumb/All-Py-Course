num=int(input("Enter a number: "))

for i in range(1,11):
  # print(str(num) + " X " + str(i) + " = "  + str(i * num))
  print(f"{num} X {i} = {num*i}") # This is called "f" Strings

print("Soo, this was the table of", num)
