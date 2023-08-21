# List
my_list = [1, 2, 3, 4]
print("List:")
print("Original List:", my_list)
my_list.append(5)
print("After appending 5:", my_list)
my_list.remove(3)
print("After removing 3:", my_list)
print()

# Tuple
my_tuple = (1, 2, 3)
print("Tuple:")
print("Tuple element at index 1:", my_tuple[1])
print()

# Set
my_set = {1, 2, 3, 4}
print("Set:")
print("Original Set:", my_set)
my_set.add(5)
print("After adding 5:", my_set)
my_set.remove(3)
print("After removing 3:", my_set)
print()

# Dictionary (Dict)
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary:")
print("Original Dictionary:", my_dict)
my_dict['gender'] = 'Female'
print("After adding gender:", my_dict)
del my_dict['age']
print("After removing age:", my_dict)
print()
