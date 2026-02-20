
"""#Day 6

##Q. Find sum of first 100 odd number.
"""

sum = 0
count = 0

for i in range(10000):
 if i%2 !=0:

  sum   = sum + i
  count = count + 1

  if count== 100:
   print("The Sum of odd number is : ", sum)
   break

"""##Prime Number"""

#basic
n = 7
c = 0

for i in range(1,n+1):
  if n%i == 0:
   c +=1

if c == 2:
    print("prime")
else:
    print("Not Prime")


## 7  = (1,2,3,4,5,6,7) c = 2
## 6  = (1,2,3,4,5,6) c = 4
## 13 = (1,2,3,4,5,6,7,8,9,10,11,12,13) c = 2

#basic2

n = 7
c = 0

for i in range(2,n):
  if n%i == 0:
   c +=1

if c == 0:
    print("prime")
else:
    print("Not Prime")


## 7  = (2,3,4,5,6) c = 0
## 6  = (2,3,4,5) c = 2
## 13 = (2,3,4,5,6,7,8,9,10,11,12) c = 0

#prime number optimised for more digit

n = 8
c = 0

for i in range(2,n):
  if n%i == 0:
   c += 1

  if c==1:
    break

if c == 1:
    print("Not Prime")
else:
    print("Prime")


## 7  = (2,3,4,5,6) c = 0
## 6  = (2,3,4,5) c = 2
## 13 = (2,3,4,5,6,7,8,9,10,11,12) c = 0

