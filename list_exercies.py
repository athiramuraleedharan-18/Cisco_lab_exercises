numbers=[111, 1, 7, 2, 1]
print("Original list: ",numbers)
#Length of list
print("Length of list: ",len(numbers))
#Removing elements from a list.
del numbers[1]
print("Length post removing an element from the list: ",len(numbers))
print(numbers)

'''
print(numbers[4])
numbers[4]=1
results in
IndexError: list index out of range

'''

#print the last element in the list: negative indices
print("The last element in the list: ", numbers[-1])

#print the 2nd last element in the list
print("The 2nd last element in the list: ",numbers[-2])


#Adding elements to a list
numbers=[111,7,2,1]
print(len(numbers))
print(numbers)


##Append or add a number to the end of the list

numbers.append(4)
print(len(numbers))
print(numbers)


##Insert an element at the beginning of the list
numbers.insert(0, 222)
print(len(numbers))
print(numbers)


##Insert an element at index 1  of the list
numbers.insert(1, 333)
print(len(numbers))
print(numbers)
