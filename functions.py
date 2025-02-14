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
