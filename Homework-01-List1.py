print("Hello" , "\n" )

a = int(input("Enter a number please > "))
b = int(input("Enter another number please > "))
c = int(input("Enter another number > "))
d = int(input("Enter another > "))

numbers = [a , b , c , d]
print("Here are your numbers you have entered : " , numbers)

numbers.sort()
print("Here are your numbers you have entered in order : " , numbers)

e = int(input("Now , enter a number again to add to your numbers > "))
numbers.append(e)
numbers.sort()
print("Here are your numbers again with your new number in order : " , numbers)

numbers.remove(a)
numbers.remove(e)
print("We removed the first and the last number you have entered ." , numbers)
print("The first :" , a , "\n" , "The last one :" , e)

f = int(input("Now , enter your new number to insert in the numbers  > "))
insert = int(input("Please enter the order you want to inser (e.g : 1 ) > "))

numbers.insert(insert-1 , f)

print("Here are your numbers after we inserted the number you entered : " , numbers)

print("Here are your numbers after all changes : " , numbers)
