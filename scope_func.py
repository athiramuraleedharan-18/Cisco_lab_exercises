#scope
#a variable existing outside a function has scope inside the functions body

def my_function():
  print("Do I know that variable?", var)

var=1
my_function()
print(var)

#inside function var shadowing outside function
def my_function():
  var=2
  print("Do I know that variable?", var)

var=1
my_function()
print(var)

#global keyword

def my_function():
  global var
  var=2 #no new variable inside is created instead outside variable is used ...global scope
  print("Do I know that variable?", var)

var=1
my_function()
print(var)
