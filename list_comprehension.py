#List comprehension
#copy the entire list
list_1 = [1]
list_2 = list_1[:]#if no start and end mentioned by default entire list is considered
list_1[0]=2
print(list_2)


#Copying some parts of list
my_list=[10,8,6,4,2]
new_list=my_list[1:3]
print(new_list)

#slices - negative indices
my_list=[10,8,6,4,2]
new_list=my_list[1:-1]
print(my_list)
print(new_list)

