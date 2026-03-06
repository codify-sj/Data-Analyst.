 """#Day 7

##Q. Create a list with numbers between 1 to 10 and the values should be squared
"""

##[1,4,9,16...]

lst = []

for i in range (1,11):
  lst.append(i**2)

print(lst)

"""##Q. Create a list with numbers between 1 to 100 and the value should contain only even numbers?"""

lst = []

for i in range(1,101):
  if i%2 == 0:
   lst.append(i)
print(lst)

"""##List Comprehension

* Basics syntax [expression for item in iterable]
* with conditional logic [expression for item in iterable if condition]
* Nested List Comprehension [ expression for item1 in iterable1 for item2 in iterable2]

###* Basics syntax [expression for item in iterable]
"""

#1
lst = []

for i in range(10):
  lst.append(i)
print(lst)

#2
lst = []

for i in range(10):
  lst.append(i**2)
print(lst)

"""* Basics syntax [expression for item in iterable]"""

#1 List Comprehension
lst = [i for i in range(10)]

print(lst)

#2 List Comprehension
lst = [i**2 for i in range(10)]

print(lst)

"""###* with conditional logic [expression for item in iterable if condition]"""

#1 Basic code from above # without List Comprehension

for i in range(1,101):
  if i%2 == 0:
   lst.append(i)
print(lst)

"""* with conditional logic [expression for item in iterable if condition]"""

lst = [i for i in range(1,101) if i%2 == 0] #we are added if condition and its doing append
print(lst)

#Basic
for i in range (1,7):
  for j in range (1,7):
    print(i,j)

lst = [(i,j) for i in range (1,7) for j in range (1,7)]
print(lst)

fruits = ['apple','mango','kiwi','orange','banana','banana']

fruits.append("Watermelon")
print(fruits)

fruits.insert(1,'avacado')
print(fruits)

fruits.reverse()
print(fruits)

popped_value = fruits.pop()
print(popped_value)
print(fruits)

fruits.remove('banana')
print(fruits)

"""###Slicing Concept"""

fruits = ['apple','mango','kiwi','orange','banana']

fruits [1:2]

fruits [0:4:2] #start:stop:step

"""### List within list

#### 1D list
"""

lst [23,34,25,[43,56,76],[34,56,76,[12,34,45]],46,76]

"""####2D List"""

lst =[[1,2,3],
      [4,5,6],
      [7,8,9]]

      # (0,1)
      # (0,2)
      # (0,3)
      # (1,1)
      # (1,2)

len(lst)

for i in range(len(lst)):
 print(lst[i])

for i in range(len(lst)):
 for j in range(len(lst)):
   print(lst[i][j])

"""sqaure matrix"""

lst =[[1,2,3,3],
      [2,3,4,6],
      [5,6,3,5],
      [3,5,7,7]]

len(lst)

for i in range(len(lst)):
 print(lst[i])

for i in range (len(lst)):
  for j in range(len(lst)):
    print(lst[i][j], [i],[j])

