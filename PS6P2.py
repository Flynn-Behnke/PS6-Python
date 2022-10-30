count = 1
num1 = 1
num2 = 1
print(num1)
print(num2)
while count <= 18:
  new = num1+num2
  print(new)
  num1 = num2
  num2 = new
  count = count+1
