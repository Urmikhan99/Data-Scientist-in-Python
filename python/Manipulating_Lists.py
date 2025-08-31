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