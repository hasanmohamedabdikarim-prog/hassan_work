name =  str ("Hassan")
age  =  str ("how old  i'm")
age  =  int (24)

height_m = str ("what is my height in cm?")
height = float (187)

print("name: "+ name)
print("age:",age)
print("height in  cm:",height)
print(type(age))
print (type(height))

height_in_meter = height /100
print ("height in meters:",height_in_meter)


if 5 > 2: 
    print("five is greater than two") 
print(3 * 5)
print (30000000)
print ("maymuun she_is, 13 years old")
print("hello guys!",end=" ")
print ("i will post it on youtube." )
x = 'ayman'
# variable names 
myvar = "deko"
myvar2 = "isse"
x,y,z = "orange","banana","water milon"
print (x)
print (y)
print (z)

x = y = z ="orange"
print(x)
print (y)
print (z)   

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "python"
y = "is"
z = "awesome "
print (x,y,z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "john"
print (x,y)

x = "awesome"
def myfunc():
   print ("python is " + x)
   myfunc()

   x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = 5+6j
y = -7
y = 9.0

x = 3+5j
y = 5
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 8.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#casting strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print ("i'ts alright ")
print ("he is called 'mohamed'")
print ('she is called "amina"')

a = "Hello"
print(a)

a = """ .lorem ipsum dolor sit  amet,consectetur adipiscing elit,....."""
print (a)

a = '''lorem ipsum dolor sit  amet,consectetur adipiscing elit,...'''
print (a)

#Strings are Arrays
#Get the character at position 1
#remember that the first character has the position 0:

a = "hello,mohamed"
print (a[1])

for x in "banana":
  print(x) 
a = "hello,hassan!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "the best things in life are free!"
if "free" in txt: 
   print("yes,'free'is present ")

   txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing Strings not understood well!!!!
b = "Hello, World!"
print(b[2:5])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, HASAN "
print(a.strip()) # returns "Hello, World!"

a = "WLO, Hawo!"
print(a.replace("W", "H"))

a = "salaan, soomaliweyn!"
b = a.split(",a")
print(a)

a = "haye"
b = "hassan"
c = a + b
print(c)

a = "haye"
b = "hassan"
c = a + " " + b
print(c)

# f-string methode
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# place holder

price = 60
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)
#You will get an error if you use double quotes
#  inside a string that is surrounded by double quotes:
#txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"walaalah\"from the north."
print(txt)

# BOOLEANS
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  print(bool("Hello"))
print(bool(150))

x = "YOOO"
y = 30

print(bool(x))
print(bool(y))

#some values are true 
bool("abc")
bool(5555)
bool(["apple", "cherry", "banana"])
#some values are false 
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  x = 200
print(isinstance(x, int))
print (10 + 5 )
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1)
print(sum2)
print(sum3)
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
#the walrus opretor
numbers = [1, 2, 3, 4, 5 , 6]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

    #Python Ternary Operator
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)
num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

#Python Comparison Operators
#Operator	     Name	                       Example
#==	           Equal            	         x == y	
#!=	          Not equal	                   x != y	
#>          	Greater than	                 x > y	
#<           	Less than	                   x < y	
#>=	        Greater than or equal to	     x >= y	
#<=	        Less than or equal to	x        <= y

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
#Chaining Comparison Operators
x = 5

print(1 < x < 10)

print(1 < x and x > 10)
# logical operator 
#Operator	 Description	           Example
#and 	  Returns True if both 
 #       statements are true	x          < 5 and  x < 10
#or      Returns True if one of the      x < 5 or x < 4
  #      statements is true
  # not	 Reverse the result, returns False
  #    if the result is true	not     (x < 5 and x < 10) 

x = 5
print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))
x = 5

print(not(x > 3 and x < 10))
#python identity operators
# is: returns true if both variables are the same obejct e.g xis y
# is not : returns true if both variables are not the same obejct e.g x is not y    
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)
#Difference Between is and ==
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
#Python Membership Operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Python Bitwise Operators?...............
print(6 | 3)
#Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 4 * 4)
print(5 + 4 - 7 + 3)
 #Lists
thislist = ["apple", "banana", "water milon"]
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
mylist = ["apple", "banana", "cherry"]

print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist = ["apple", "banana", "lemon"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["lemon", "banana", "w.melon", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)
thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)

thislist = ['apple','melon','cherry']
thislist.insert(2,'watermelon')

print (thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["watermelon", "banana", "cherry"]
del thislist
thislist = ["apple", "banana", "cherry"]
thislist = ['man','baby','tree']
thislist.pop(2)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
thislist = ["deek", "ahmed", "hawo"]
for x in thislist:
  print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
thislist = ["mohamed", "deek", "da'uud"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#?????????????
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in fruits]
newlist = [x for x in fruits]
newlist = [x for x in range(10) if x < 5]
#Expression
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
#Sort List Alphanumerically
thislist = ["youtube", "circle", "girl", "schoool", "23"]

thislist.sort()

print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
hislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"]
#pyhton copy lists
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
thistuple = ("w.melon", "banana", "cherry", "apple", "cherry")
print(thistuple)
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple

thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
tuple1 = ("abc", 34, True, 40, "male")
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#access tuble
thistuple = ("apple", "penapple", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:2])
#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  #python update tubles
  x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) #this will raise an error 
#because the tuple no longer exists


#unpack tubles
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", 'melon', "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#python loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  #join tuples
  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# pyhton sets 
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: 
# the items will appear in a random order.

# Refresh this page to see the change in the result.
thisset = {"apple", "banana", "cherry", "apple"}
# duplicates not allowed
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
thisset = {"apple", "banana", "cherry" , "mango"}

print(len(thisset))
set1 = {"w.melon", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
# set types
print(set1)
print(set2)
print(set3)
set1 = {"abc", 34, True, 40, "male"}
myset = {"apple", "banana", "cherry"}
print(type(myset))
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will
#  display the items in a random order.
# access items
thisset = {"oman", "iraq", "en"}

for x in thisset:
  print(x)
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) 
thisset = {"apple", "banana", "cherry"}
# add items 
print("banana" not in thisset)
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#remove set items 
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#thisset = {"apple", "banana", "cherry"}

#del thisset

#print(thisset)
#pyhon loop sets 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  # join sets 
  set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
set1 = {"gold", "banana", "cherry"}
set2 = {"google", "microsoft", "gold"}

set1.intersection_update(set2)
print(set1)
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
#frozenset()
x = frozenset ({"apple","mango","kiwi"})
#display x:
print (x)

#display the data type of x:
print (type(x))
#Dictionaries 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["year"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
#From Python's perspective, dictionaries are 
#defined as objects with the data type 'dict':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)
# access items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

color_key = "color"
car[color_key] = "red"

print(x) #after the change
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

year_key = "year"
car[year_key] = 2020

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

color_key = "color"
car[color_key] = "red"

print(x) #after the change
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the " 
  "thisdict dictionary")
  #change dictionary 
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2020

print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)
#Add Dictionary 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)
#remove items 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#thisdict =	{
 # "brand": "Ford",
  #"model": "Mustang",
#"year": 1964
#del thisdict
#print(thisdict) #this will cause an error 
#because "thisdict" no longer exists.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# loop through a dictionary 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1960
} 
for x, y in thisdict.items():
  print(x, y)
  #COPY
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#Nested dictionaries 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
#python if ELse 
a = 33
b = 200

if b > a:
  print("b is greater than a")
  number = 15

if number > 0:
  print("The number is positive")
  age = 20


if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
  is_logged_in = True

if is_logged_in:
  print("Welcome back!")
 # PYHTON ELIF STATEMENT 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
  #python else

  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
  # PYTHON SHORTHAND IF 
a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330

print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330 

print("A") if a > b else print("=")if a == b else print ("B")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
# Logical operators in python 
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

  a = 33
  b = 200
  if not a >b:
    print ("a is not greater then b")

    age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

  temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

  username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

  score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")
  #Nested if 
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

  score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

    temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")


score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")
  #The pass statement
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without 
# the pass statement

age = 20

if age < 18:
  pass  # TODO: Add underage logic later
else:
  print("Access granted")

score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass  # Zero case - no action needed
else:

  def calculate_discount(price):
    pass
#Match
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

    day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    # python while loop

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

  #For loop
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  for x in "banana":
    print(x) 

fruits = ["apple","banana","cherry"]
for x in fruits:
  print (x)
  if x == "bananan":
    break

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

  for x in range(2, 30, 3):
    print(x)

  for x in range(6):
    print(x)
else:
  print("Finally finished!")

  for x in range (6):
    if x == 3: break
    print (x)
  else: 
    print("finally finished")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    #for x in [0, 1, 2]:
  #pass

# having an empty for loop like this, would raise 
# an error without the pass statement
# python functions 
#A function is a block of code which only runs when it is called.

#A function can return data as a result.

#A function helps avoiding code repetition.

def my_function():
  print("Hello from a function")

my_function()

def my_function():
  print ("hello from a function ")

my_function()
my_function()
my_function()

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

def get_greeting():
  return "Hello from a function"

print(get_greeting())
#Python Function Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name,
#inside the parentheses. You can add as many arguments as you 
#want, just separate them with a comma.

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

def my_function():
  return["apple","banana","cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

def my_function(name, /):
  print("Hello", name)

my_function("Emil")

def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

def my_function(*, name):
  print("hello", name)

  my_function(name = "Emil")

def my_function(a,b,/,*,c,d):
  return a+b+c+d

result = my_function(5, 10, c = 20 , d = 30)
print(result)
#python * Args and ** Kwargs
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

def my_fuction(greeting, *names):
  for name in names:
    print(greeting, name)

my_fuction("hello","emil","tobias",'linus')

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print("  ", key + ":", value)



my_function("emil123", age = 25, city = "Oslo", 
            hobby = "coding")

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: 
my_function(fname="Emil", lname="Refsnes")
#scope
def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

def myfunc():
  global x
  x = 300

myfunc()

print(x)

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
#Decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "hello " + nam

print(myfunction("john"))

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
#lambda
x = lambda a: a + 10
print(x(5))

x = lambda a,b : a * b
print(x(5,6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2)) 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie","banana","cherry"]
sorted_words = sorted(words , key =lambda x: len(x))
print(sorted_words)
#Recursion 
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n -2)

print(fibonacci(7))

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

import sys
print(sys.getrecursionlimit())
#python generators
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
#print(next(gen)) # This will raise StopIteration

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)


def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
#PYTHON ARRAYS
#get the first item
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)

cars = ["FORD","VOLVE","BMW"]
cars[0] = "Toyota"

print(cars)

cars = ["ford","volvo","BMW"]

x = len(cars)

print (x)

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)

  cars = ["Ford", "Volvo", "BMW"]

cars.append("TOYOTA")

print(cars)

cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)


cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)
#pyhon Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

  mystr = "banana"

  for x in mystr:
    print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 25:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#python OOP
class MyClass:
  x = 5

print(MyClass)

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class MyClass:
  x = 5

  p1 = MyClass()
  p2 = MyClass()
  p3 = MyClass()

  print (p1.x)
  print (p2.x)
  print (p3.x) 
#python_init_ method
class Person:
  def _init_(self, name, age):
    self.name = name
    self.age = age

    p1 = Person("John", 36)

    print(p1.name)
    print(p1.age)
    #Default Values in __init__()
    class Person:
     def __init__(self, name, age =18):
      self.name = name
    self.age = age

def new_func(Person):
    return p1

p1 = new_func(Person)
#p2 = Person("Tobias", 25)

#print(p1.name, p1.age)
#rint(p2.name, p2.age)
#Multiple Parameters
class Person:
  def __init__(self,name, age, city , country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

    p1 = Person("Emil", 36, "Oslo", "Norway")

    print(p1.name)
    print(p1.age)
    print(p1.city)
    print(p1.country)
    #Self Parameter
    class Person:
      def __init__(self, name, age):
       self.name = name
      self.age = age  

      def greet(self):
        print("Hello, my name is " + self.name)

        p1 = Person("john",30)
        p1.greet()

        class Person:
          def __init__(self, name):
            self.name = name

  def printname(self):
    print(self.name)

#p1 = Person ("Tobias")
#p2 = Person ("Linus")

#p1.printname()
#p2.printname()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("John", 30)
p1.greet()

# Accessing properties with self
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.make} {self.model} {self.year}")


car1 = Car("Toyota", "Camry", 2020)
car1.display_info()

# Calling methods with self
class WelcomePerson:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def greet(self):
        return "hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + " welcome to our platform!")


p1 = WelcomePerson("Tobias")
p1.welcome()
#class properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
#accessing class properties
class car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

    car1 = car("toyota", "camry", 2020)

print(car1.make)
print(car1.model)
print(car1.year)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error

class Person:
  species = "Human"  # Class property

  def __init__(self, name):
    self.name = name  # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    return f"Hello, my name is {self.name}."

  def get_info(self):
    return f"{self.name} is {self.age} years old."

  def celebrate_birthday(self):
    self.age += 1
    return f"Happy birthday, {self.name}! You are now {self.age}."

  p1 = Person("Tobias", 25)

  p1.city = "Oslo"

  print(p1.name)
  print(p1.age)
  print(p1.city)
  #pyhton class methods
  class Person:
   def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    print = person("Emil", 30)
    p1.celebrate_birthday()
    p1.celebrate_birthday()
    #The __str__() Method
    class Person:
     def __init__(self, name, age):
      self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} is {self.age}"

p1 = Person("Tobias", 25)
print(p1)  # Output: Tobias is 25 years old

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    self.name = name

    def greet(self):
      print ("hello")

      p1 = Person("Emil")

      del Person.greet

      #python inheritance
      class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)

            x = Person("John", "Doe")
            x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

class person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class student(person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = student("Mike", "Olsen")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()
#pyhton polymorphism
x = "Hello World!"

print(len(x))

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
#pyhton file hinding
f = open("demofile.txt", "r")

print(f.read())

f = open("d:\\myfiles\\welcome.txt", "r")

print(f.read())

with open("demofile.txt", "r") as f:
  print(f.read())

  f = open("demofile.txt", "r")

print(f.readline())

f.close()

with open("demofile.txt", "r") as f:
  print(f.read(5))

  with open("demofile.txt") as f:
      for x in f:
       print(x)

       with open("demofile.txt", "a") as f:
        f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

  with open("demofile.txt", "w") as f:
   f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

  #This will create a new file:

f = open("myfile.txt", "x")

#If the file already exist, an error will be raised.



