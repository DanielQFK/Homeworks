# if-elif-else
# This is a program to guess your continent based on your nationality...

# So we start with greeting and saying about what we want
print("Hello" , "\n" , "Please give us information we need... " )
print("Firs of all ")
# Then we ask for nationality ...
nationality = input("Where are you from ? ")
# and after that we creat a condition that :
if nationality == "Iran" :
    print("Oh , so you are an Asian...")
    continent = "Asia"
# Iran = Asia    
elif nationality == "Ameica" :
    print("Oh , so your continent is north America...")
    continent = "north America"
# America = North America
elif nationality == "England" :
    print("Oh , so you are an Europian...")
    continent = "Europe"
# England = Europe    
elif nationality == "Brazil":
    print("Oh , so your continent is south America...")
    continent = "South America"
# Brazil = South America    
elif nationality == "Egypt" :
    print("Oh , so you are an African...")
    continent = "Africa"
# Egypt = Africa

# if the country wans't in our condition we ask to write the continet        
else:
     continent = input("what is your continent? " )     
# Then we ask name , lastname and age ...     
name = input("what is your name? ")
lastname = input("what is your lastname ? ")
age = int(input("how old are you? "))

# Then we put the information in a list
information = [name , lastname , age , nationality , continent]

# Then print based on the list
print( "\n" , "\n" , "Based on what you've entered :" , "\n" , "You are" , information[0].title() , information[1].title()
, "\n" , "And also you are " , information[2] , "years old ;" , "\n" , "And ofcourse , You are from" , information[3].title() 
, "\n" , "And the name of continent you live in is" , information[4].title() , "\n" , "\n" , "Thanks for your patience" 
, "\n" , "Don't forget to smile..." , "≧^◡^≦")


