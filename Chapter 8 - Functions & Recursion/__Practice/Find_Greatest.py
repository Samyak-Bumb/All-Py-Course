def mx(num1,num2,num3):
  if (num1>num2):
    if (num1>num3):
      return num1
    else:
      return num3


  else:
    if (num2>num3):
      return
    else:
      return num3

m=mx(26,64,69)

print("Max No. is "+str(m))
