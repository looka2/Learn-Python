a = "Python"
b = "is"
c = "awesome!"
print(a,b,c)

d = 5
e = 7
print(d*e)

x = "cool"

def myfunc():
    x = " wow!"
    print("Dit is gemaakt door Luka," + x)

myfunc()

print("Dit is heel " + x)

f = 1
g = 3.6
h = 8j

print(type(f))
print(type(g))
print(type(h))

import random
print("The Number of the day is" , random.randrange(1, 10))

def myfunc():
    x = int(1)
    y = int(2.8)
    z = int("3")
    print(x)
    print(y)
    print(z)

myfunc()

txt = "The best thing about Python is that is is easy to test code wich is cool."
if "hard" not in txt:
    print("No, 'Hard' is NOT present.")
if "hard" in txt:
    print("Yes'Hard' is present.")


def myfunc():
    a = "wow,"
    b = "python."
    c = a + " " + b
    print(c)
myfunc()

quantity = 6
itemno = 36
price = 7.99
myorder  = "I want to pay {2} for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

def myfunc():
    a = 1
    b = 7
    c = 4
    d = a+b+c
    print(d)
myfunc()

listno1 = ["apple", "banana", "apple", "grape", "Maybe a pear"]
print(listno1)

list1 = [1, 2, 3, 4, 5]
list2 = [True, True, False, True, False]
list3 = ["apple", "samsung", "Xiaomi"]
list4 = ["1", "3", "4", "6"]

print(list1)
print(list2[:2])
print(list3[2])

if "Xiaomi" in list3:
  print("Yes, 'Xiaomi' is in list3")

list4.insert(1, "2")
list4.insert(4, "5")
print(list4)

def myfunc():
    a = 6
    b = 1
    c = 18
    d = a+b
    e = d*c
    print(e)
myfunc()

def myfunc():
    x = "My"
    y = "brain"
    z = "hurts"
    print(x,y,z)
myfunc()



def wiskunde():
    m = 5
    l = 4*m+11
    print(l)
wiskunde()