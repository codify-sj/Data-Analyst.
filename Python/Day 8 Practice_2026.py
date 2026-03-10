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

counter = 0
for i in range(len(marks)):
  if (marks[i] < 33):
    counter = counter + 1
    print(subject[i],marks[i],"Failed")
  else:
    print(subject[i],marks[i],"Passed")
