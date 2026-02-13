# -*- coding: utf-8 -*-

#Day 1

##Intro to Python
"""

print("hello world")

print(123)

print("Sanju")

print('12abc')

"""DataTypes:
'''
int.
string.
boolean.
float.
'''

##Arithmetic operators

## INT-INT Operation
"""

print('12+10')

print(12-10)

print(12*10)

print(12/10)

print(12//10)

print(12%10)

print(12**10)



"""## INT-String Operation"""

print(12+ 'Harsh')

print(12-'Harsh')

print(12*'Harsh')

print(12/'Harsh')

print(12//'Harsh')

print(12%'Harsh')

print(12**'Harsh')

"""##Boolean-Boolean"""

print(False+True)

print(False-True)

print(False*True)

print(False%True)

print(False/True)

print(False//True)

print(False**True)

""" ##String-String Operation"""

print('Sanju'+ 'sanju')

print('sanju'-'sanju')

print('sanju'*'sanju')

print('sanju'/'sanju')

print('sanju'//'sanju')

print('sanju'%'sanju')

print('sanju'**'sanju')

""" ##Int-String Operation"""

print("12"+'sanju')

print('12','sanju')

print("Hi your age is:",12)

print("hi your age is:", " ", "12")

"""##Typecasting"""

print(type(12))

type("sanju")

type(12)

type(1.2)

type(True)

print(str(12)+'sanju')

print(3.14)

print(int(3.14))

print(int('sanju')) ## Int can converted to String, But String can't be converted to INT

"""## Variables

"""

abc = 12
print(abc)

a12=12
print(a12)

123abc=12 ##Invalid variable
print(123abc)

ab_c=12
print(ab_c)

_123abc=12
print(_123abc)

first_name = input("Hi write your first name")
print(first_name)

"""## Find Simple Interest"""

P = int(input("Enter Principle"))
R = int(input("Enter Rate"))
T = int(input("Enter Time"))
SI=(P*R*T)/100
print(SI)
Pnew = P+ SI
print("your Final Amount is", Pnew)

a = "Sanju"
print(a)
a = 12
print(a)
a ="12 + Harsh"
print(a)

"""##Simple Calculator

"""

num1 = int(input('give Num 1 :'))
num2 = int(input('give Num 2 :'))

add= num1+num2
print("The Addition is :", add)

sub= num1-num2
print("The Sub is :", sub)

Multi= num1*num2
print("The Multi is :", Multi)

div= num1/num2
print("The division is :", div)

