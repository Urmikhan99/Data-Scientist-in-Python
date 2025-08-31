
'''
Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
Print areas with the print() function.
'''

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas =[hall,kit,liv,bed,bath]

# Print areas
print(areas)

# subsetting lists
fam=['liz',1.73,'emma',1.68,'mom',1.71,'dad',1.89]
print(fam[6])
print(fam[2:6])
print(fam[-1])
print(fam[7])
print(fam[:4])
print(fam[5:])
'''
🔑 Short Note on List Indexing & Slicing

Positive indexing: Starts from 0 (e.g., fam[0] = 'liz')

Negative indexing: -1 gives the last element (e.g., fam[-1] = 1.89)

Slicing [start:end]: Takes elements from start to end-1

Omitted start: fam[:4] → takes from beginning to index 3

Omitted end: fam[5:] → takes from index 5 to the last element
'''
