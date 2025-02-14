#Dictionaries

dictionary={"cat":"chat", "dog":"chien", "horse":"cheval"}

phone_numbers={'boss': 5551234567, 'Suzy': 22657854310}

empty_dictionary={}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#safe searches in dictionary

words=['cat', 'lion', 'horse']

for word in words:
  if word in dictionary:
    print(word, " -> ", dictionary[word])
  else:
    print(word, " is not in dictionary" )


#Dictionary methods and functions

#keys method

for key in dictionary.keys():
  print(key,"->",dictionary[key])


for english,french in dictionary.items(): #items() returns tuples where each tuple is a key-value pair
  print(english,"->",french)


#modifying and adding values

dictionary['cat']='minou'
print(dictionary)

#sorted
for key in sorted(dictionary.keys()):
  print(key,"->",dictionary[key])
  
#values method

for french in dictionary.values():
  print(french)

#adding a new key
dictionary["swan"] = "cygne"
print(dictionary)

#can also add using update method

dictionary.update({"duck":"canard"})
print(dictionary)


#Removing a key
del dictionary['dog']
print(dictionary)

#popitem() method - to remove the last item in a dictionary
dictionary.popitem()
print(dictionary)
