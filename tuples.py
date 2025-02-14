#Tuples

#tuple creation
tuple_1=(1,2,4,8)
tuple_2=1., .5, .25, .125

print(tuple_1)
print(tuple_2)

#empty tuple
empty_tuple=()

#one-element tuple
one_element_tuple1 = (1,)
one_element_tuple1 = 1.,

#accessing tuple elements

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
  print(elem)

#operations that can be performed on tuple as they are immutable

my_tuple = (1, 10, 100)

t1= my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#tuples on left-side of the assignment operator, circulating values
var=123

t1=(1, )
t2=(2, )
t3=(3, var) #variables can be assigned as well
print(t1,t2,t3)

t1,t2,t3 = t2, t3, t1

print(t1,t2,t3)
