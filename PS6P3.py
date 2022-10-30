f = open("data.txt","r")

totbonus = 0

lastname = str(f.readline().rstrip('\n'))

while lastname != "":
  salary = float(f.readline().rstrip('\n'))
  if salary >= 100000:
    brate = 0.20
  elif salary >= 50000 and salary < 100000:
    brate = 0.15
  else:
    brate = 0.10
  bonus = brate*salary
  print("Last name:", lastname)
  print("Bonus pay:", bonus)
  print(" ")

  totbonus = totbonus + bonus

  lastname = str(f.readline().rstrip('\n'))

f.close()

print("Total bonus payout:", totbonus)
