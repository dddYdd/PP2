#1 
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2 
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3 
thislist = list(("apple", "banana", "cherry")) # 
print(thislist)
#4
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#5
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#6 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#7 
#
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#8
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#1 Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#2 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#3 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#2 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)
# 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#2 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#3 
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#3 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#4 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#2 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
