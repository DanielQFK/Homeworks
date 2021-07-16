# int-input/list/if-elif
# It's just an easy and useful exercise of int-input/list/if-elif

# In this program , I just asked 10 name and age  
name1 = input("enter the first name of the classmate > ")
age1 = int(input("enter his/her age > "))

name2 = input("enter the second name of the classmate > ")
age2 = int(input("enter his/her age > "))

name3 = input("enter the third name of the classmate > ")
age3 = int(input("enter his/her age > "))

name4 = input("enter the fourth name of the classmate > ")
age4 = int(input("enter his/her age > "))

name5 = input("enter the fifth name of the classmate > ")
age5 = int(input("enter his/her age > "))

name6 = input("enter the sixth name of the classmate > ")
age6 = int(input("enter his/her age > "))

name7 = input("enter the seventh name of the classmate > ")
age7 = int(input("enter his/her age > "))

name8 = input("enter the eithth name of the classmate > ")
age8 = int(input("enter his/her age > "))

name9 = input("enter the nineth name of the classmate > ")
age9 = int(input("enter his/her age > "))

name10 = input("enter the tenth name of the classmate > ")
age10 = int(input("enter his/her age > "))

name11 = input("enter the eleventh name of the classmate > ")
age11 = int(input("enter his/her age > "))


# And put the names in a list with a .title()
names = [name1.title() , name2.title() , name3.title() , name4.title() , name5.title() , name6.title() , name7.title() , name8.title() , name9.title() , name10.title() , name11.title() ]

# put the ages in a list too
ages = [age1 , age2 , age3 , age4 , age5 , age6 , age7 , age8 , age9 , age10 , age11]

print("Here are your names : " , names)
print("Here are your ages :" , ages)

# now sort the names in order of alphabet
names.sort()
print( "\n" , "Here are the names in order :" , names)

# now sort the ages in order
ages.sort()
print("Here are the ages in order" , ages)

# print the lowest and the highest age
print( "\n" , "The lowest age is : " , ages[0])
print("The highest age is : " , ages[10] )

# calculate the average
average = (age1+age2+age3+age4+age5+age6+age7+age8+age9+age10+age11)/11
print( "\n" , "The average of the ages is : " , average)

# explain a condition if the age is higher than average , just remove it...
if age1 > average :
    ages.remove(age1)
elif age2 > average :
    ages.remove(age2)
elif age3 > average :
    ages.remove(age3)
elif age4 > average :
    ages.remove(age4)
elif age5 > average :
    ages.remove(age5)
elif age6 > average :
    ages.remove(age6)
elif age7 > average :
    ages.remove(age7)
elif age8 > average :
    ages.remove(age8)
elif age9 > average :
    ages.remove(age9)    
elif age10 > average :
    ages.remove(age10)
elif age11 > average :
    ages.remove(age11)
    
else:
    print("ERROR !")
    
print(ages)  
