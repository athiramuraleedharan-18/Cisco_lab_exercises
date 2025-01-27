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
