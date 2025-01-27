#Lab eexercise - The basics of list

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print(hat_list)

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
mid = len(hat_list) // 2
print("Middle of the list: ", hat_list[mid])
hat_list[mid]=int(input("Enter an integer number to be replaced with the middle number: "))
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
print("Length of the existing list: ", len(hat_list))
print(hat_list)

