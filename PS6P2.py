num1 = 0
num2 = 1
print(num1)
print(num2)
for x in range (1,20,1):
  new = num1+num2
  print(new)
  num1 = num2
  num2 = new
