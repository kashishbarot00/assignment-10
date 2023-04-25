def discount(qty, price, discrate):
  total = (qty * price)
  discamt = discrate * total
  discprice = total - discamt 

  return discamt,discprice




qty = float(input("Enter the Quantity:"))
price = float(input("Enter the Unit Price $ "))
discrate = float(input("Enter the Discount rate %"))
discamt,discprice = discount(qty, price, discrate)

print("This is yout quantity " ,qty)
print("The unit price $ " ,price)
print("This is your discounted amount $ ",discamt)
print("This is your discounted price $ " ,discprice)