# int-input/if-elif-else...
# this is a program to calculate the payment of workers and whose salary is below than 
# the average we add 1.000.000 more ...

# so at first we say what we are going to do
print("Hello" , "Please do what we tell you ")
print("IMPORTANT TIP : PLEASE ENTER THE MONEY BY 'TUMAN' " , "\n" )

# Then we start asking about each person's name and salary
worker1 = input("Enter the name of worker number one > ")
salary1 = int(input("please enter how much he/she gets salary > "))

worker2 = input("Enter the name of worker number two > ")
salary2 = int(input("please enter how much he/she gets salary > "))

worker3 = input("Enter the name of worker number three > ")
salary3 = int(input("please enter how much he/she gets salary > "))

worker4 = input("Enter the name of worker number four > ")
salary4 = int(input("please enter how much he/she gets salary > "))

worker5 = input("Enter the name of worker number five > ")
salary5 = int(input("please enter how much he/she gets salary > "))

worker6 = input("Enter the name of worker number six > ")
salary6 = int(input("please enter how much he/she gets salary > "))

worker7 = input("Enter the name of worker number seven > ")
salary7 = int(input("please enter how much he/she gets salary > "))

worker8 = input("Enter the name of worker number eight > ")
salary8 = int(input("please enter how much he/she gets salary > "))

worker9 = input("Enter the name of worker number nine > ")
salary9 = int(input("please enter how much he/she gets salary > "))

worker10 = input("Enter the name of worker number ten > ")
salary10 = int(input("please enter how much he/she gets salary > "))

# Then we make them title() in a list...
workers = [worker1.title() , worker2.title() , worker3.title() , worker4.title() , worker5.title() , worker6.title() , worker7.title() , worker8.title() , worker9.title() , worker10.title()]

# then print the name of workers with a capital letter ...
print( "\n" , "Here are the workers of your company : " , "\n" ,  workers)

# After that append the slaries in another list...
salaries = [salary1 , salary2 , salary3 , salary4 , salary5 , salary6 , salary7 , salary8 , salary9 , salary10]

# Then print the list of salaries
print( "\n" , "And here are the salaries they are paid : " , "\n" , salaries )

# Now , to be clear , we print them in a way to be able to see each one's name and salary
# exactly next to each other... 
print(  "\n" , "The workers and their salaries (by Tuman) : " , "\n" ,
workers[0] , " gets " , salary1 , "\n" , 
workers[1] , " gets " , salary2 , "\n" , 
workers[2] , " gets " , salary3 , "\n" , 
workers[3] , " gets " , salary4 , "\n" , 
workers[4] , " gets " , salary5 , "\n" , 
workers[5] , " gets " , salary6 , "\n" , 
workers[6] , " gets " , salary7 , "\n" , 
workers[7] , " gets " , salary8 , "\n" , 
workers[8] , " gets " , salary9 , "\n" , 
workers[9] , " gets " , salary10)

average = (salary1+salary2+salary3+salary4+salary5+salary6+salary7+salary8+salary9+salary10)/10
print( "\n" , "Here is the average of the salaries : " , average)

add = 1000000

if salary1 <= average :
   salaries[0] = salary1 + add
if salary2 <= average :
   salaries[1] = salary2 + add
if salary3 <= average :
   salaries[2] = salary3 + add
if salary4 <= average :
   salaries[3] = salary4 + add
if salary5 <= average :
   salaries[4] = salary5 + add
if salary6 <= average :
   salaries[5] = salary6 + add
if salary7 <= average :
   salaries[6] = salary7 + add
if salary8 <= average :
   salaries[7] = salary8 + add
if salary9 <= average :
   salaries[8] = salary9 + add
if salary10 <= average :
   salaries[9] = salary10 + add
        
print( "\n" , "We  added 1.000.000 tuman to the workers' salary which was lower the average :) ")
print("And here are the workers' salary after the changes : " , "\n" , salaries)

if salary1 > average :
    salaries.remove(salary1)
    workers.remove(worker1.title())
if salary2 > average :
    salaries.remove(salary2)
    workers.remove(worker2.title())
if salary3 > average :
    salaries.remove(salary3)
    workers.remove(worker3.title())
if salary4 > average :
    salaries.remove(salary4)
    workers.remove(worker4.title())
if salary5 > average :
    salaries.remove(salary5)
    workers.remove(worker5.title())
if salary6 > average :
    salaries.remove(salary6)
    workers.remove(worker6.title())
if salary7 > average :
    salaries.remove(salary7)
    workers.remove(worker7.title())
if salary8 > average :
    salaries.remove(salary8)
    workers.remove(worker8.title())
if salary9 > average :
    salaries.remove(salary9)
    workers.remove(worker9.title())
if salary10 > average :
    salaries.remove(salary10)
    workers.remove(worker10.title())
# Read the below line(It's the explanation of what I have done...)
print( "\n" ,  "And also we removed the workers with their salary who get salary higher than the average :( " , "\n" , 
"And here are the workers in a line and their salary exactly under them in order : " , "\n" , workers , "\n" , salaries)


    
print( "\n" , "And finally , here are the remain of the workers and their salaries (Exactly) under them , after the changes :" , 
"\n" , workers , "\n" , salaries) 

print( "\n" , "Thanks for your patience... ")
