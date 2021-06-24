#This program is about Binary.To calculate binary of a number :

I = []
#At first we make an empty list
number = int(input("Please enter a number > "))
#Then start the process by asking number
number=number*2
#after that , we multiply in 2 
for x in range(10):
#Then we put it in loop to devide our number
    number = number/2
    x = number%2
    #Because in Binary remainder is concidered we calculate that by %
    if number<1:
        break
    #We continue untill quotient be equaled to 1 or 0
    I.append(x)
    #As you see we add the remainders in our list we have made
I.reverse()
#and because the numbers are not in order weuse (reverse) to make it in order
print(I)    

    
