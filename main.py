# Data Structures and Algorithms in Python Hardcover – 5 July 2013
# by Roberto Tamassia (Author), Michael H. Goldwasser (Author) Solutions
# 1.12 Exercise page 51 
---------------------
# ---R-1.1 

def is_multiple(n,m):
  try:
    if n%m==0:
      print("Multiple")
    else:
      print("Not a multiple")
  except ZeroDivisionError:
    print("Cant divide by zero")

# ---R-1.2
--1st solution
is_multiple(101,99)
is_multiple(3,3)
is_multiple(3,0)

def is_even():
  num=input("Please enter the number ")
  if num[-1]=='2' or num[-1]=='4' or num[-1]=='6' or num[-1]=='8' or num[-1]=='0':
    print("Yes its even")
  else:
    print("Not even")



# ---2nd solution using regex
import re
def is_even():
  num=input("Input the number: ")
  mode=re.compile(r'(2)|(4)(6)|(8)|(0)$')
  if mode.search(num):
    print("Even")
  else:
    print("Not even")

# --- R-1.3
# Without using sort
def minmax(data):
  min=data[0]
  max=data[0]

  for i in data:
    if i<min:
      min=i
    elif i>max:
      max=i
    else:
      continue
    
  return (min,max)

lst=[]

nu_of_seq_lements=int(input("Enter the number of elements in sequence: "))
for i in range(nu_of_seq_lements):
  x=int(input())
  lst.append(x)

print(minmax(lst))
print("min,max")

# --- R-1.3
Using sort

def minMax(x):
  sorted_x=sorted(x)
  return (sorted_x[0],sorted_x[-1])

lst=[]
nu_of_seq_lements=int(input("Enter the number of elements in sequence: "))
for i in range(nu_of_seq_lements):
  x=int(input())
  lst.append(x)

print(minMax(lst))

# --- R-1.4

def sum_under_n(n):
  x=0
  for i in range(n):
    x+=i**2
  print(x)

sum_under_n("Input ur number here")

# --- R-1.5

def sum_under_n(n):
  total= sum([i**2 for i in range(n)])
  return total

print(sum_under_n(10))

# --- R-1.6

def odd_sum_square_under_n(n):
  total=0
  for i in range(n):
    if(i%2!=0):
      total+=i**2
    else:
      continue
  return total
  
print(odd_sum_square_under_n(5))


# --- R-1.7

def odd_sum_square_under_n(n):
  total=sum([i**2 for i in range(n) if i%2!=0])
  return total
print(odd_sum_square_under_n(5))

# --- R-1.8

lst=[1,2,3,4,5,6]
k=-3
print("lst[k]: " ,lst[k])

j = k + len(lst)
print("lst[j]: ",lst[j])

# --- R-1.9

print([i for i in range(50,90,10)])

# ---R-1.10

print([i for i in range(8,-10,-2)])

# ---R-1.11

print([2**i for i in range(9)])

# ---R-1.12

from random import randrange

def random_number(x,y):
    return randrange(x, y+1, 5)

print(random_number(10,100))

# ---R-1.13

def reverser(lst):
  lst=lst[::-1]
  return lst

lst=[1,2,3,4,5]
print(reverser(lst))

# ---R-1.14

def odd_pair(lst):
  extralst=[i for i in lst if i%2!=0]
  return extralst
lst=[1,2,3,4,5,6,8,7,9,10]
print("The possible pair is :",odd_pair(lst))

# ---R-1.15

def distinct_Checker(lst):
  if len(lst)==len(set(lst)):
    return True
  else:
    return False

lst=[1,2,3,4,5,6,23,123]
lst1=[1,12,1,12,323,232131,31231]
print(distinct_Checker(lst))
print(distinct_Checker(lst1))

# ---R-1.18

lst=[x*(x+1) for x in range(10)]
print(lst)

# ---R-1.19

lst=[chr(i) for i in range(97,123,1)]
print(lst)

# ---R-1.20

from random import randint
def shuffle(lst):
  i=randint(0,len(lst)-1)
  return lst[i]

print(shuffle(["abc","ababa","10sd","dasndajsn"]))

# ---R-1.21

def takeInput():
  data=[]
  while(True):
    try:
      data.append(input())
    except EOFError:
      break
  data.reverse
  return data

print(takeInput())

# ---R-1.22

def dot_product(a,b):
  if len(a)==len(b):
    c=[a[i]*b[i] for i in range(len(a))]
    return c
  else:
    print("Len not equal.")

a=[1,2,3]
b=[12,2,3]
print(dot_product(a,b))

# ---R-1.23

def out_of_bound(data):
  try:
    for i in range(len(data)+1):
      print(data[i])
  except IndexError:
    print("Don’t try buffer overflow attacks in Python!")
lst=[1,2,3,4,5]
out_of_bound(lst)

# ---R-1.24

from collections import Counter

def vowelCount(str):
  s=Counter(str)
  print(s)

vowelCount("dnsakjndkjandadksa")

# ---R-1.25

import string
def punchRemover(s):
  s=s.translate(str.maketrans('', '', string.punctuation))
  return s
print(punchRemover("I don't have any idea!."))

# ---R-1.26

def correctArithmetics(a,b,c):
  if(a+b==c):
    print("It passed the first case.")
  else:
    print("It failed the first case")
  if(a==b-c):
    print("It passed the second case.")
  else:
    print("It failed the second case")
  if(a*b==c):
    print("It passed the third case.")
  else:
    print("It failed the third case")
  print("\n\n\n")

correctArithmetics(1,2,3)
correctArithmetics(56,2,3)
correctArithmetics(1,3,3)

# ---R-1.27
def factors(n): # generator that computes factors
  k=1
  lst=[]
  while k*k < n: # while k < sqrt(n)
    if n % k == 0:
      yield k
      lst.append( n // k)
    k += 1
  if k*k == n: # special case if n is perfect square
    yield k
  for i in sorted(lst):
    yield i

for i in factors(100):
  print(i)

# ---R-1.28

from math import sqrt
def p_norm(v,p):
  x=eucledian_norm=0
  for i in v:
    eucledian_norm+=i**2
    x+=i**p
  return (sqrt(x),sqrt(eucledian_norm))

print(p_norm([1,2,3],2))

# ---R-1.29

from itertools import permutations
given_chars=['c','a','t','d','o','g']
l=list(permutations(given_chars,len(given_chars)))
for i in l:
  print(''.join(i))

# ---R-1.30

def divide_by_2(num):
  count=0
  while num>2:
    print(num)
    num=num/2
    count+=1  
  return count+1

print(divide_by_2(10))

# ---R-1.31

def cash_returned(amt_given,amt_charged):
  if amt_given<amt_charged:
    return "Amount not enough sir"
  else:
    return_amt=amt_given-amt_charged
    notes_of_ten=return_amt//10
    return_amt=return_amt-notes_of_ten*10
    notes_of_five=return_amt//5
    return_amt=return_amt-notes_of_five*5
    notes_of_50_paisa=return_amt//0.5
    return_amt=return_amt-notes_of_50_paisa*0.5
  return(notes_of_ten,notes_of_five,notes_of_50_paisa)
print(cash_returned(100,19))

# ---R-1.32

def calculator(num1,num2,operator):
  if(operator=="+"):
    return num1+num2
  if(operator=="-"):
    return num1-num2
  if(operator=="//"):
    return num1//num2
  if(operator=="/"):
    return num1/num2
  if(operator=="%"):
    return num1%num2

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
operator=input("Enter the operator")

print(calculator(num1,num2,operator))

# ---R-1.34

from random import randint
str_to_spam="I will never spam my friends again"

def spammer():
  for i in range(100):
    swapIndex=0
    swappedIndex=0
    while(swapIndex==swappedIndex):
      x=(list(str_to_spam))
      swapIndex=int(randint(0,len(str_to_spam)-1))
      swappedIndex=int(randint(0,len(str_to_spam)-1))

   
    char_1=x[swapIndex]
    char_2=x[swappedIndex]
    
    x[swapIndex]=char_2
    x[swappedIndex]=char_1

    print(i+1,"".join(x))

spammer()

# ---R-1.35
import random

def birthday_paradox(n):
  lst=['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November','December']
  lst_bds=[]
  for i in range(n):
    birth_month=random.choice(lst)

    if(birth_month in "January, March, May, July, August, October, and December"):
      birth_date=random.randint(1,31)
    else:
      birth_date=random.randint(1,30)

    if(birth_month=="February"):
      birth_date=random.randint(1,29)
    
    print("Person 1 birthdate and month is ", birth_date, birth_month)

    if(str(birth_date)+birth_month in lst_bds):
      print("Match found",birth_date,birth_month)

    lst_bds.append(str(birth_date)+birth_month)
    # print(str_1)

birthday_paradox(25)

# ---R-1.36

from collections import Counter
def word_counter():
  strings=input("Enter the words seperated by spaces: ")
  strings=strings.split(' ') 
  print(Counter(strings).most_common())
  

word_counter()
  
