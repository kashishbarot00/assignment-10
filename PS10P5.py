total = 0.0
tax = 0.0
def comptotal(qty,price):
   global total
   total = qty * price
   global tax 
   tax = total * 0.07
   return


qty = float(input("Enter quantity of item: "))
price = float(input("Enter price per unit: "))
comptotal(qty,price)

print("Your total is $ " , format(float(total), '10,.2f'))
print("Tax cost is $ " , format(float(tax), '10,.2f'))


   
