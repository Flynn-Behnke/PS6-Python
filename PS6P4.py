f = open("data.txt","r")

item = str(f.readline().rstrip('\n'))

order = 0
totextprice = 0
while item != "":
  quant = int(f.readline().rstrip('\n'))
  price = float(f.readline().rstrip('\n'))
  extprice = quant*price
  print(item)
  print("Price per unit:", price)
  print("Quantity:", quant)
  print("Extended price:", extprice)
  print(" ")
  order = order+1
  item = str(f.readline().rstrip('\n'))
  totextprice = totextprice+extprice
  
f.close()

print("Sum of all the extended prices:", totextprice)
print("Number of orders:", order)
print("The average order:", totextprice/order)
