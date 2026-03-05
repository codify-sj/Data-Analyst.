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

fruits = ['apple','mango','kiwi','orange','banana']

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

