fam=["liz",1.73,"emma",1.68,"mom",1.71,"dad",1.89]

fam=fam +["me",1.79]

fam_ext = fam + ["me,1.79"]
# Adds "me" and 1.79 to the end of the list.

del fam[-1]
print(fam)


x=["a","b","c"]
y=x
y[2]="p"
# This changes the 3rd element (index 2) of the shared list from "c" → "p".
print (y)
# Lists are mutable → You can change them after creation.



x=["a","b","c"]
y=list(x)
y=x[:]
y[1]="z"
print(y)


'''Update the area of the bathroom to be 10.50 square meters instead of 9.50 using negative indexing.
Make the areas list more trendy! Change "living room" to "chill zone". Don't use negative indexing this time.
'''
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4]="chill zone"
print(areas)



'''
Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.
'''

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas+["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1+["garage",15.45]
print(areas_1)
print(areas_2)



'''
Delete the string and float for the "poolhouse" from your areas list.
Print the updated areas list.
'''

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 
        20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10:12]

# Print the updated list
print(areas)
