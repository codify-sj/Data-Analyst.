 """#Day 8"""

marks = [23,45,34,56,77,56]
subject = ['English','Hindi','Punjabi','Physics','Chemistry','Python']



"""##Find the average marks the sudent has scored"""

s = 0

for i in range (len(marks)):
  print(marks[i])
  s = s + marks[i]

print("Average Marks :" , s/len(marks))

for i in range (len(marks)):
  print(subject[i],marks[i])

"""##Check if the student failed un any exam. Count the frequency."""

marks = [23,45,34,56,77,22]
subject = ['English','Hindi','Punjabi','Physics','Chemistry','Python']
counter = 0
for i in range(len(marks)):
  if (marks[i] < 33):
    counter = counter + 1
    print(subject[i],marks[i],"Failed")
  else:
    print(subject[i],marks[i],"Passed")

marks = [23,45,34,56,77,22]
subject = ['English','Hindi','Punjabi','Physics','Chemistry','Python']
failcount = 0
passcount = 0
print("---------Subject-Marks----------")
for i in range(len(marks)):
  if (marks[i] < 33):
    failcount = failcount + 1
    print(subject[i],marks[i],"Failed")

  else:
    passcount = passcount + 1
    print(subject[i],marks[i],"Passed")
print("--------------------------------")
print("Total Failed Students:",failcount)
print("--------------------------------")
print("Total Passed Students:",passcount)

"""##Create a Credit History"""

# 80 - 100 A+
# 60 - 80  B
# 50 - 60  C
# 40 - 50  D
# Else F

marks = [23,45,34,56,77,22]
subject = ['English','Hindi','Punjabi','Physics','Chemistry','Python']
for i in range(len(subject)):
   if marks[i]>= 80:
    print(subject[i],marks[i], "A+")
   elif marks[i]>= 60:
    print(subject[i],marks[i], "B")
   elif marks[i]>= 50:
    print(subject[i],marks[i], "C")
   elif marks[i]>= 40:
    print(subject[i],marks[i], "D")
   else:
    print(subject[i],marks[i], "F")



"""Matrix"""

lst =[[1,2,3,3],
      [2,3,4,6],
      [5,6,3,5],
      [3,5,7,7]]
for i in range (len(lst)):
  for j in range(len(lst)):
    print(lst[i][j], [i],[j])

"""## Sum of diagonal elements of a matrix"""

#i value
# (0,0)
# (1,1)
# (2,2)
# (3,3)
lst =[[1,2,3,3],
      [2,3,4,6],
      [5,6,3,5],
      [3,5,7,7]]

for i in range(len(lst)):
  for j in range(len(lst)):
    if lst[i] == lst[j]:
     print(lst[i][j], [i],[j])

"""##Tuple"""

tup = ()
print(type(tup))

tup = (1,2,3,3.23,34.65,"vidit",True)
print(tup)

#Tuple is immutable: we cannot change elements after creation , ## unordered unique value
#tup(2) = "sanju"

"""##Sets"""

s = {1}
print(type (s))

s = {1,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,45,6,76,56,45,456}
print(s)



#Counting Unique words in text

word = "This is the class of set Tuple Dictonary and today we will finish core Python"
a = word.split()
print(a)

"""## Q. Find the unique words in it"""

words = 'this class class does contain contain some python python Classes classes'

a = word.split()
a = set(a)
print(a)

"""##Dictionary"""

dct = {}
print(type(dct))
print(type(s))

dct = {1:"Harsh",2: "Vidit", 3: "Ansh"}
print(dct)

print(dct.keys())
print(dct.values())
print(dct.items())

dct = {
    "Roll_No": [1,2,3,4,5],
    "Name": ["harsh","Vidit","Ansh","Chinmoy","Amit"]
}

dct = {1:'Harsh',2:'Amit',3:'Chinmoy',4:'Vidit'}
print(dct)

for i in dct.items():
  print(i)

for i in dct:
  print(dct[i])

dct = {
    "Roll_No": [1,2,3,4,5],
    "Name": ["harsh","Vidit","Ansh","Chinmoy","Amit"]
}

students = {
    101: {"name": "Aman", "age": 19, "course": "BCA", "year": 1},
    102: {"name": "Riya", "age": 20, "course": "BBA", "year": 2},
    103: {"name": "Karan", "age": 21, "course": "B.Tech", "year": 3},
    104: {"name": "Neha", "age": 19, "course": "BSc", "year": 1},
    105: {"name": "Rahul", "age": 22, "course": "BA", "year": 4}
}

for i in students:
  print(i,students[i],['name'])

for i in students:
 print(students[i])

print(len(students))

for i in range(len(students))
