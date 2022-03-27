def fact(p):
  product=1

  for i in range(p):
    product=product*(i+1)

  return product

f=fact(3)

print(f)
