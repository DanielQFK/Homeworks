#if-elif Homework
# Its just a program to tell you if your parents are old or young...

# age1 = int(input("Please enter your age <=> "))
# age2 = int(input("Now , please enter you parent's age <=> "))

# mines = age2 - age1

# if mines < 14 :
#     print("You have made a mistake." , "\n" , "please correct it...")
# if 14 <= mines < 20  :
#     print("You have so young parent. ")
# if mines > 20 :
#     print("You have old parent. ")
# if mines == 20 :
#     print("Your parent's age is fit. ")
    
# print("\n" , "Thanks for your patience... ≧^◡^≦ ")

#.................Both programs are the same but this is better:...........................

#First of all we say something to greet...
print("Hello" , "\n" , "Please enter the information which we need :")

# w eget 2 int-input = one of them your age / another your parent's age...
age1 = int(input("Please enter your age > "))
age2 = int(input("Please enter your parent's age > "))
Standard = 15 # The standard minus of your age and your parent is 15

# Calculate the minus of your age and your parent...
mines = age2 - age1

# and we have some conditions that you can see
if mines < Standard :
    print("The information you have entered is incorrect" , "\n" , "please correct it...")
elif mines <= 20 : 
    print("Depending on your age , your parent is so young... ")
elif 20 < mines < 40 :
    print("Based on your age , your paren's age is fit...")
elif 55 > mines >= 40 :
    print("Depending on your age , your paren is a almost old...")
elif mines >= 55 :
    print("Based on your age your parent is so old...")
    
print("\n" , "Thanks for your patience...  ≧^◡^≦ "  ) 
