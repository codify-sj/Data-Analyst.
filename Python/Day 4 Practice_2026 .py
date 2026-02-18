
"""#Day 4

##Q. Calculate and employee's bonus based on their performance rating and years of service.
"""

## rating>4.5
  ## yrs>10
    ##20%

  ##yrs> 5
    ##10%

  ##rating >3.5
   ##yrs>10
   #10%

   ## yrs>5
    ## 5%
  ## else no bonus

salary = int(input("Give Salary"))
rating = float(input("Give rating :"))
yrs    = int(input("Give years of experince : "))

bonus = 0   # default bonus

if (rating>4.5):
  if (yrs >= 10):
    bonus = 20
  elif (yrs >=5):
    bonus = 10
elif (rating>3.5):
   if (yrs>=10):
    bonus = 10
   elif (yrs>5):
    bonus = 5
   else:
    bonus = 0


final_salary = (salary + ((bonus/100)*salary))
print("Hi your bonus % is" , bonus, "Your Final Salary is", final_salary)


################Conditional################################

"""##Loops

"""

range(10)

for i in range(10):
 print(i)

for i in range(1,10):
 print(i)

for i in range(1,11):
 print(i)

for i in range(1,10,2):
 print(i)

"""##5 Table"""

for i in range(5,51,5):
 print(i)

"""##Table 3"""

num = 3
for i in range(3,30+1,3):
  print(i)

"""##Table 7"""

num = 7
for i in range(7,70+1,7):
  print(i)

"""##Table 11"""

num = 11
for i in range (11,110+1,11):
  print(i)

"""##General loop for table"""

num = 15
for i in range(num,num*10+1,num):
  print(i)

num = int(input("Please enter table you want to know about : "))
for i in range(num,num*10+1,num):
  print(i)

"""##Reverse Table"""

for i in range(10,0,-1):
  print(i)

for i in range(50,0,-5):
  print(i)

##Generalised
num = 12
for i in range(num*10,num-1,-num):
  print(i)

"""##Q. Find number between 1 to 100 and are divisible by both 3 and 5"""

for i in range (1,101):
 if (i%3 == 0 and i%5== 0):
  print(i)

"""##Q. Count the number between 1 to 100 and are divisible by both 3 and 5"""

count=0
for i in range(1,101):
  if (i%3 ==0 and i%5==0):
    new_count = count+1
    print(i, new_count)

"""##Q. find the sum of first N natural numbers."""

# (n*(n+1))/2

counter = 0
for i in range(1,11):
  counter = counter + i
print(counter)

N = 20
counter = 0
for i in range(1,N+1):
  counter = counter + 1
print(counter)

"""##Q Find first 10 numbers between 1 and 10,000 those who are divisible by 3,5 and 7"""

Counter = 0
for i in range (1,1000):
 if (i%3 == 0 and i%5 == 0 and i%7 == 0):
  counter += 1 #counter = counter + 1
  print(i)

 if (counter == 10):
  break
