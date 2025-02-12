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

#list comprehension
list_1=[1]
list_2=list_1 #instead of contents memory reference is copied here
list_1[0]=2
print(list_2)
#copying the entire list
list_3=list_1[:] #slice operation , here only contents are copied as a brand new list
list_1[0]=3
print(list_3)

#copying some parts of the list
my_list=[10,8,6,4,2]
new_list=my_list[1:3]
print(new_list)

#negative indices with slice.
new_list=my_list[1:-1]
print(new_list)

#del instruction
del my_list[1:3]
print(my_list)

#deleting contents all at once from a list
del my_list[:]
print(my_list)
#here list becomes empty

#by removing slice in above the whole list gets deleted.
del my_list
print(my_list)

#To check for greater value in the list
'''my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest=my_list[0] #Compare the rest of the elements with largest

for i in range(1,len(my_list)):
  if my_list[i] > largest:
    largest = my_list[i]

print(largest )'''

my_list=[17, 3, 11, 5, 1, 9, 7, 15, 13]
largest=my_list[0]
'''
for i in my_list: #here the 1st element is compared to it unnecessarily
  if i > largest:
    largest = i
print(largest)'''

#Find the location of an element in a list
my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find=5 #element to be searched for in the list
found=False #flag

for i in range(len(my_list)):
  found=my_list[i]==to_find
  if found:
    break

if found:
  print(str(to_find)+" found at index : "+str(i))
else:
  print("absent")


#to avoid that we can use slicing
for i in my_list[1:]:
  if i > largest:
    largest = i
print(largest)

#Calculate hits in a draws in a bet.
'''
Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.

The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.

The question is: how many numbers have you hit?
'''

drawn=[5, 11, 9, 42, 3, 49]
bets=[3, 7, 11, 42, 34, 49]
hits=0

#check for elements in bets that are in drawn

for number in bets:
  if number in drawn:
    hits+=1

print(hits)

