# buils-in functions
# list methods
fam=['liz',1.73,'emma',1.68,'mom',1.71,'dad',1.89]
print(fam.index("mom"))

print(fam.count(1.73))

'''
 list object methods short note
🔹 .index(x) → Shows the index (position) of the first occurrence of x in the list.
🔹 .count(x) → Counts how many times x appears in the list.
'''

# str methods
sister='liz'
print(sister.capitalize())
print(sister.replace("z","sa"))


# method 2

fam=['liz',1.73,'emma',1.68,'mom',1.71,'dad',1.89]
fam.append("me")
print(fam)
'''
Key Points:

append(x) adds element x at the end of the list.

It modifies the list in-place.

Does not return the updated list → calling print(fam.append("me")) gives None.
'''

# String Methods

'''
Use the .upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
Print out place and place_up. Did both change?
Print out the number of o's on the variable place by calling .count() on place and passing the letter 'o' as an input to the method. We're talking about the variable place, not the word "place"!
'''

# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()


# Print out place and place_up
print(place)
print(place_up)


# Print out the number of o's in place
print(place.count('o'))

'''
Strings are immutable → .upper() returns a new string, original stays the same.
'''
