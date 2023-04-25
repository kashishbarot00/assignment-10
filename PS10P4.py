def b_avg (score1,score2,score3,handi):
 sum = score1 + score2 + score3
 avg = (sum/3) 
 havg = (sum + handi) / 3

 return avg,havg


lname = str(input("Enter bowlers last name: "))
score1 = float(input("Enter your score 1: "))
score2 = float(input("Enter your score 2: "))
score3 = float(input("Enter your score 3: ")) 
handi = float(input("What is your Handicap: "))
avg,havg = b_avg (score1,score2,score3,handi)

print("Your Last name: " ,lname)
print("Yor average score is: " ,avg)
print("Your Handicap: " ,havg)
