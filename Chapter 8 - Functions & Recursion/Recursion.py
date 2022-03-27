def fact_r(p):
  if p==1 or p==0:
    return 1

  return p*fact_r(p-1)

f=fact_r(3)

print(f)
