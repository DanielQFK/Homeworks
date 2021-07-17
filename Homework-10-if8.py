# int-input/if-elif-else
# This program is just to show that if someone can be accepted in a school based on a special condition
print("Hello , depending on your scores we accept or we don't accept to our school...")
# In this program Math and Average is important
Math = int(input("Enter your Math score please > "))
Average = int(input("Enter uyour average > "))

print("Your average is" , Average)
print("and your Math is " , Math) 
# Now write your condition...
if Math == 20 or Average >= 19.5:
    print("You are accepted...")
elif Math >= 18 and Average >=16:
    print("You are accepted...")
elif Math >= 14 and Average >= 18:
    print("You are accepted...")
else:
    print("You are failed...")   
    b
