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
