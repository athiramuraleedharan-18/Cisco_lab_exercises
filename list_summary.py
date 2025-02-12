#Summary list
#simple assignment of a list would make the variable point to the same memory location

vehicles_one=['car','bicycle','motor']
print(vehicles_one)

vehicles_two=vehicles_one
del vehicles_one[0]
print(vehicles_two)

#To copy a list or part of a list - slicing

colors=['red', 'green', 'orange']
copy=colors[:] #copies the entire list
copy1=colors[0:2] #copies part of the list

print(colors)
print(copy)
print(copy1)


#Negative indices to perform slicing
sample_list=["A", "B", "C", "D", "E"]
new_list=sample_list[2:-1] #-1 represents the last element
print(sample_list,new_list,sep="\n")

#optional start and end in slicing
my_list=[1,2,3,4,5]
slice_one=my_list[2:]#start is 2 and end is len(my_list)-1 by default
slice_two=my_list[:2]#start is 0 by default and end is 2 here
slice_three=my_list[-2:]#start is 2nd last element and end is len(my_list)-1 by default


print(slice_one)#[3,4,5]
print(slice_two)#[1,2]
print(slice_three)#[4,5]


#delete slices using del instruction
del my_list[0:2]
print(my_list)#[3,4,5]

del my_list[:]#delete all the elements in the list and make the list empty
print(my_list)


#To check if elements exist or not in list using membership operators in and not in
my_list=['A',"B",1,2.0]

print("A" in my_list)#True
print('C' not in my_list)#True
print(2 not in my_list)#False
