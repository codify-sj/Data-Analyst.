

"""#Day 2

##Q. Find compound Interest
"""

p  = int(input("Please enter principle balance : "))
r  = int(input("Give interest rate: "))
t  = int(input("Give number of time periods elapsed: "))
n  = int(input("Give number of times interest applied per time period: "))

amount= p * ((1+r/n))**(n*t)
print ("Your Coumpond Interest value is : ", amount)

"""##Q. Find volume of cylinder"""

r = float(input( "Please enter radius : "))
h = float(input( "Please enter height : "))
vol = 3.14 * (r)**2 *(h)
print("The volume is :", vol)

"""##Conditional Statements

"""

print("Sanju")

"""###Find if the age is eligible for voting

[-infinity - 0] - Invalid [0-17] - Minor [18-100] - Eligible [100 - infinity] - Invalid
"""

age = int(input("Enter your age: "))

if (age>= 18 and age <=100):
 print("Eligible")
elif(age>=0 and age<18):
  print("Minor")
else:
  print("Invalid")

"""### **Indentation**"""

if True:
  print("hey")

if True:
  if True:
   print("hey")
print("Yo")

if True:
  if True:
    if False:
      print("hey1")
      print("heyy2")
  print("hey")
print("Yo")

age = 19

if (age<18):
 print ("Hey")
 if (age >17 and age <20):
  print("Yo")
  print("Hello")
print("Final")

age = int(input("Enter your age: "))

if (age>= 18):
  if(age <100):
   print("Eligible")
elif(age>=0):
  if(age<18):
    print("Minor")
else:
  print("Invalid")

"""##Q. Find if the number is even or odd"""

a = int(input("Give Number:"))

if( a % 2 == 0):
 print("Its Even")
else:
  print("Its odd")

"""## Q. Find if number is +ve. if yes then find if it is even or odd else tell -ve."""

num = int(input("Give number"))
if num > 0 :
   print("number is +ve")
   if num % 2 == 0:
     print("Number is even")
   else:
    print("number is odd" )
else:
  print ("Number is -ve")

