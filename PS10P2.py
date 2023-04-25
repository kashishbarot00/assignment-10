def examavg (exam1 , exam2 , exam3):
 sum = exam1 + exam2 + exam3
 total = 300
 percent = (sum/total) * 100
 avg = (sum/3)
 points = exam1 + exam2 + exam3 

 return avg,points



lname = str(input("Enter your last name: "))
exam1 = float(input("Enter your exam 1 score: " ))
exam2 = float(input("Enter your exam 2 score: " ))
exam3 = float(input("Enter your exam 3 score: " ))

avg,points = examavg (exam1 , exam2 , exam3)
print("Your Last Name: " ,lname)
print("Your exam score average is: " ,avg)
print("Your total points is:" ,points)

