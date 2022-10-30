sb = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate in decimal form: "))
totintamt = 0
for y in range (1,6,1):
  intamt = sb*rate
  eb = sb+intamt
  totintamt = totintamt+intamt
  print("Year", y)
  print("Starting balance:", sb)
  print("Interest amount:", intamt)
  print("Ending balance:", eb)
  sb = eb
print("Total interest amount:", totintamt)
