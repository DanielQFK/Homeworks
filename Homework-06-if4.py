# if-elif-else 
# This is a program to calculate the average of your marks
# At first we start saying what we are going to do...
print("Hello")  
print("This program has been made to tell you the average of your lessons based on your marks ")

# then we ask for your marks by int-input...
math = int(input("Please enter you math mark > "))
science = int(input("Please enter you science mark > "))
PhysicalEducation = int(input("Please enter you P.E mark > "))
literature = int(input("Please enter you literature mark > "))
religion = int(input("Please enter you religion mark > "))
art = int(input("Please enter you art mark > "))
sociology = int(input("Please enter you sociology mark > "))

# Now we calculate the average...
average = (math+science+PhysicalEducation+literature+religion+art+sociology)//7
print("Your average is = " , average)
 # and finally we say our conditions...
if average > 20 :
    print("You have made a mistake , please correct it...")
elif average == 20 :
    print("Oh , come on , You have the best mark in the class...≧^◡^≦ ")
elif 18 <= average < 20 :
    print("Very good , you have a good mark...≧°◡°≦")
elif  14 <= average < 18 :
    print("Good , not bad , work harder...(◕‿◕✿")
else:
    print("It's not good , you need to work harder...")
    
a    
