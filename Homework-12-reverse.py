# A program to reverse any number you give...
 
print("Hello , here we are to get your number and reverse it and again give it to you... ")
Input = int(input("So please just enter your number > ")) #The first Input to get the number...

# We need two valuable to help us hold valuesin them(I will mantion something duriong the duration)
First_helper_valuable = 0 # To give a value to our valuable to make it known for the continues of the program...
Second_helper_valuable = 0 # the same as the above line
# we also say a condition that if number was below zero , say ...
if Input <= 0:
    print("You have entered a wrong number")
        
# we use while to stop that when our name during the duration bacome zero...
while Input>0:

    # At first to calculate the reversed number we need the remaining number of the Input
    First_helper_valuable = Input%10 

    #Then we need to add it to the second helper value ,(It's what I wanted to mention)
    # Because we want to devide the Input and it will become 0 so we need to add the value to another valuable to save that...
    Second_helper_valuable = Second_helper_valuable+First_helper_valuable 

    #Now we multiplie it in 10 because it should be easy to add more numbers to this valuable not 1+2 but 10+2=12 
    Second_helper_valuable = Second_helper_valuable*10 

    #Now we devide the Input in 10 because we want to get a number from it and give to second helper valuable(remaining number) so if
    #  we want to back to the  beggining of the program and not get the same remaining number we should devide it...
    Input = Input//10 

Second_helper_valuable = Second_helper_valuable//10 # Now if we get the output a 0 has added to our number and to remove that we devide it in 10
print("Here is your number reversed : " , Second_helper_valuable)    # And finally we print that... .
