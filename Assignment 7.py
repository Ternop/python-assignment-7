# Andrew Ternopolsky
# Task 1 - Working with Lists

# Step 1: Create a list of favorite fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", fruits)

# Step 2: Append a new fruit
fruits.append('fig')
print("After adding a fruit:", fruits)

# Step 3: Remove one fruit
fruits.remove('apple')  # You can choose which fruit to remove
print("After removing a fruit:", fruits)

# Step 4: Print list in reverse order using slicing
reversed_fruits = fruits[::-1]
print("Reversed list:", reversed_fruits)


# Task 2 - Exploring Dictionaries

# Step 1: Create a dictionary about yourself
person = {
    "name": "Alice",
    "age": 25,
    "city": "Toronto"
}

# Step 2: Add a new key-value pair
person["favorite color"] = "Blue"

# Step 3: Update the city
person["city"] = "New York"

# Step 4: Print all keys and values using a loop
print("\nKeys and Values:")
for key, value in person.items():
    print(f"{key}: {value}")


# Task 3 - Using Tuples

# Step 1: Create a tuple with favorite movie, song, and book
favorites = ("Inception", "Bohemian Rhapsody", "1984")
print("\nFavorite things:", favorites)

# Step 2: Try to change one element (this will be skipped because it's not allowed)
try:
    favorites[0] = "Interstellar"
except TypeError:
    print("Oops! Tuples cannot be changed.")

# Step 3: Print the length of the tuple
print("Length of tuple:", len(favorites))
