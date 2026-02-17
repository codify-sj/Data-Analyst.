
"""#DAY: 3

##Divisible by 5 etc
"""

num = 24

if(num%5 == 0 and num%3 ==0):
 print("Divisible by 5 and Divisible by 3")
elif (num%5 ==0 and num%3 !=0):
 print("Divisible by 5 and Not Divisible by 3")
elif(num%5 != 0 and num%3 ==0):
 print(" Divisble by 3 but not by 5")
else:
  print("Not divisible by 5 and 3")

"""## Divisible by 5 (Nested) ## ques


"""

num = 24

if(num%5 == 0):
  if(num%3 ==0):
   print("Divisible by 5 and Divisible by 3") #Q.
elif (num%5 ==0):
  if(num%3 !=0):
   print("Divisible by 5 and Not Divisible by 3")
elif(num%5 != 0):
   if (num%3 ==0):
     print(" Divisble by 3 but not by 5")
else:
  print("Not divisible by 5 and 3")

"""## Q.Determine a person's stage of life (child, teen,adult,senior) based on age.

####### Child (-0 to -12)
####### Teen (-13 to 17)
####### Adult (-18 to 60)
####### Senior (-60+)
"""

age = int(input ("Please enter your age: "))
if (age>=0 and age<13):
  print("this is Child")
if(age>=13 and age<18):
  print("this is teen")
if(age>=18 and age<61):
  print("This is adult")
if(age>=61):
  print("this is senior")
else:  ## invalid is also working in 60 age
  print("invalid")

age = int(input ("Please enter your age"))
if(age>60):
  print('This is senior')
elif(age>=18):
  print("this is adult")
elif(age>=13):
  print("this is teen")
elif(age>=0):
  print("this is child")
else:
  print("invalid")



"""##Q. A simple user login system that checks the username and password."""

stored_user = "user@123"
stored_pass = "abc@123"

username = input("Please enter Username: ")
password = input("Please enter Password: ")

if(username == stored_user):
  if (password == stored_pass):
      print("login Sucessfull")
  else:
      print("Invalid Password")
else:
 print("Invalid Username")

"""##Q. Report Card Generator

#### 91-100 ->A
#### 81-90  ->B
#### 71-80  ->C
#### 61-70 ->D
#### 51-60  ->E
#### Else  Fail
"""

name  = input("Please enter your Name: ")
marks = int(input("Please enter marks: "))
if(marks> 90 and marks<=100):
 print(name + "Your Grade is A")
elif(marks> 80 and marks<=90):
   print(name + "Your Grade is B")
elif(marks> 70 and marks<=80):
  print(name + "Your Grade is C")
elif(marks> 60 and marks<=70):
  print(name + "Your Grade is D")
elif(marks> 50 and marks<=60):
  print(name + "Your Grade is E")
else:
  print( name + "Failed")



name  = input("Please enter your Name: ")
marks = int(input("Please enter marks: "))
if(marks>= 91):
  grade = "A"
elif(marks>= 81):
  grade = "B"
elif(marks>= 71):
  grade = "C"
elif(marks>= 61):
  grade = "D"
elif(marks>= 51):
  grade = "E"
else:
  grade = "Failed"
print (name + " " + "Your Grade is: " + grade)

"""##Q. Create a simple calculator"""

num1 = int(input("Please enter Number 1 : "))
num2 = int(input("Please enter Number 2 : "))

op = input("Enter operator eg: (+, -, *, / :)")
if (op == "+"):
 print(num1 + num2)
elif (op == "-"):
 print(num1 - num2)
elif (op == "*"):
  print(num1 * num2)
elif (op == "/"):
  if(num2 == 0):
    print("Invalid operation")
  else:
    print(num1 / num2)
else:
  print("Invalid")
