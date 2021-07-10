# if
# this program was my Homework ... to guess a number
# at first I identify my number you should guess
number = 16
# Then write int-input to recieve your guess
number1 = int(input("Please guess a number between 1 and 20 >"))

if number1 < 16 :
    # if it was higher than my number it tells you 
    print("enter a higher number please")
if number1 > 16 :
    # if it was lower than my number it tells you
    print("enter a lower number please ")
if number1 == 16 :
    # and if it was the same my number it tells you
    print("Congratulation , you entered the right number ")
    
# and I repeated it for three times , it means you have three chances to guess my number
number1 = int(input("Please guess a number between 1 and 20 >"))

if number1 < 16 :
    print("enter a higher number please")
if number1 > 16 :
    print("enter a lower number please ")
if number1 == 16 :
    print("Congratulation , you entered the right number ")
    
number1 = int(input("Please guess a number between 1 and 20 >"))    

if number1 < 16 :
    print("enter a higher number please")
if number1 > 16 :
    print("enter a lower number please ")
if number1 == 16 :
    print("Congratulation , you entered the right number ")
# Finished...    
