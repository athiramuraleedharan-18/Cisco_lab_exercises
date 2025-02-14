#Functions

#simple function demo

def message():
  print("Enter a value:")

message()
a=int(input())

message()
b=int(input())

print(a,b,sep=",")

def hello(name): #defining a function
  print("Hello ",name) #Body of the function


name=input("Enter your name:")

hello(name) #calling/invoking the function

def message(number):
  print("Enter a number: ",number)

number=1234
message(1)
print(number)

#Positional parameter passing

def my_func(a,b,c):
  print(a,b,c)

my_func(1,2,3)

#Positional parameter passing

def introduction(first_name,last_name):
  print("Hello, my name is ",first_name, last_name)


introduction("John","Doe")
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

#Keyword argument passing

def introduction(first_name,last_name):
  print("Hello, my name is ",first_name, last_name)


introduction(last_name ="John",first_name="Doe")
introduction(first_name="Luke", last_name="Skywalker")

