#Argument passing

#positional argument passing
def subtra(a,b):
  print(a-b)

subtra(5,2)
subtra(2,5)

#keyword(named) argument passing

subtra(a=5,b=2)
subtra(b=2,a=5)

#mixed positional and keyword argument passing
subtra(5,b=2)
#PS: 1st positional parameters have to be given followed by keyword ..order matters here

#Pre-defined or parametrized functions
def name(first_name,last_name="Smith"):
  print(first_name, last_name)

name("Andy")#Takes last_name by default as "Smith"
name("Betty", "Johnson")#"Johnson" shadows the default value.


def add_numbers(a,b=2,c):
  print(a+b+c)

add_numbers(a=1,c=3) #Results in syntax error i.e. parameter without a default follows parameter with a default.
