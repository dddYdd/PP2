x = 5
y = "John"
print(x)
print(y)

#2
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#3 
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#4 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)