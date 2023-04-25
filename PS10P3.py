def salesreport (sales):
  if sales > 100000.00:
    per = 0.10


  elif sales <= 100000.00:
    per = 0.05
  commision = sales * per
  nextyears = sales * 1.05
  return commision,nextyears 

salesper = input("Enter sales person name: ")
lname = input("Enter last name: ")
sales = float(input("Enter sales amount "))
commision,nextyears = salesreport (sales)

print("This is your Commission" ,commision)
print("This is your Next years report:" ,nextyears)