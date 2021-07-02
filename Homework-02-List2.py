children = ["Reza" , "Zahra" , "Ali" , "Mohammad" , "Hossein"]
print("These are the names : " , children)
children.sort()
print("The names in order : " , children)

add = input("enter a name to add to these names > ")
children.append(add.title())
print("The names + the name you entered : " , children )
children.sort()
print("The names + the name you entered(in order) : " , children)

add1 = input("enter a name to put it in the second order  > ")
children.insert(1 , add1.title())
print("The names with the name you just entered : " , children)
children.sort()
print("The names with the name you just entered(in order) : " , children)

children.remove("Reza")
print("we removed 'Reza' from the list : " , children)
children.sort()
print("And finally , the list of the names after all changes : " , children)