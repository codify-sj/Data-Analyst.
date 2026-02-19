
"""#Day 5"""

s ="sajan kumar"
for i in s:
  print(i)

"""##Q. Print only the vowels from a given string using a For loop."""

s ="Sajan kumar"
v ="aeiouAEIOU"
for i in s:
 if i in v:
  print(i)

s = input("Give Name : ")
v = "aeiouAEIOU"
for i in s:
  if i in v:
    print (i)

"""##Pattern Printing

"""

num = 6
for i in range(num):
  print("*"*i)

num = 6
for i in range(1,num+1):
  print("*"*i)

for i in range (1,6):
  print("* "*i)

num = 6
for i in range (1,num+1):
  print("* "*i)

num = 6
for i in range(num,0,-1):
  print("* "*i)

num = 5
for i in range(1,num+1):
 print("* "*num)

num = 5
for i in range (1,num+1):
  print("* "*i)

for i in range(num,0,-1):
  print("* "*i)

num = 10
print("A"*num)
for i in range (num-2):
  print ("|" +" "*(num-2)+ "|")

print("A"*num)

num = 10
print("*"*1)

for i in range(1, num-2):
 print("*" + " "*i+ "*")

print("*"*num)

"""##Prime Number"""

n = 6
counter = 0

for i in range(1,n+1):
  if n%i == 0:
   counter +=1

if counter == 2:
    print("prime")
else:
    print("Not Prime")

