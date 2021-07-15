# int-input/list/if-elif-else
# This program has been written to get 11 ages and sort them and each one of them was lower than average 
# will be removed...

# At first we get 11 int-input to ask ages...
age1 = int(input("enter first age > "))
age2 = int(input("enter second age > "))
age3 = int(input("enter third age > "))
age4 = int(input("enter forth age > "))
age5 = int(input("enter fifth age > "))
age6 = int(input("enter sixth age > "))
age7= int(input("enter seventh age > "))
age8= int(input("enter eighth age > "))
age9 = int(input("enter nineth age > "))
age10 = int(input("enter tenth age > "))
age11 = int(input("enter eleventh age > "))

# And make a list and put themm in list...
ages = [age1 , age2 , age3 , age4 , age5 , age6 , age7 , age8 , age9 , age10 , age11]
# And sort them...
ages.sort()
print("The ages in order > " , ages)

# Calculate the average...
average = (age1+age2+age3+age4+age5+age6+age7+age8+age9+age10+age11)/11
print("and the average is " , average)

# Explane a condition for each one , if they were lower than average remove them... 
if age1 > average :
    ages.remove(age1)
if age2 > average :
    ages.remove(age2)
if age3 > average :
    ages.remove(age3)
if age4 > average :
    ages.remove(age4)
if age5 > average :
    ages.remove(age5)
if age6 > average :
    ages.remove(age6)
if age7 > average :
    ages.remove(age7)
if age8 > average :
    ages.remove(age8)
if age9 > average :
    ages.remove(age9)    
if age10 > average :
    ages.remove(age10)
if age11 > average :
    ages.remove(age11)
    
# Then print the ages that are lower than average (Because those have been removed in condition)...    
print( "\n" , "The ages less than the average : " , ages)    
