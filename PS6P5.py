f = open("data.txt","r")

lastname = str(f.readline().rstrip('\n'))

totaltuition = 0
students = 0
while lastname != "":
  dcode = str(f.readline().rstrip('\n'))
  credits = int(f.readline().rstrip('\n'))
  if dcode == 'I':
    cost = 250.00
  else:
    cost = 500.00
  tuition = cost*credits
  totaltuition = totaltuition+tuition
  print(lastname)
  print("District code:", dcode)
  print("Credits taken:", credits)
  print("Tuition cost:", tuition)
  print(" ")
  students = students+1
  lastname = str(f.readline().rstrip('\n'))
f.close()

print("Total tuition owed:", totaltuition)
print("Number of student:", students)
