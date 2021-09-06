"""
Three classes of three cars:
1. BMW    2. Benz   3. Chevrolet
They all have three same options and two special option that are special for the car brand
"""
# Class number 1:
class BMW:

    # To calculate number of people who want to buy a car...
    Number_of_Buyers = 0
    
    # A def that included Name , ... of buyer...
    def __init__(self , Name , Last_name , Age , Id_number , Car):
        # Put them in self. to make them unlocal
        self.Name = Name
        self.Last_name = Last_name
        self.Age = Age
        self.Id_number = Id_number
        self.Car = Car
        BMW.Number_of_Buyers +=1 
        print(f"Hello mr/ms {Name} \n Based on Your choice , your car is {Car} , You have chosen an attractive car , you won't regret...(◕‿-)...\n")
     # another def to ask about the model of car...
    def Model(self):
        model_of_your_car = int(input("Enter the model that you want please (from 2000 to 2021) > "))
        if model_of_your_car < 2000 or model_of_your_car > 2021:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it...(◡‿◡✿)...")
        while model_of_your_car<2000 or model_of_your_car>2021:
            model_of_your_car = int(input("Enter the model that you want please (from 2000 to 2021) > "))
            if model_of_your_car < 2000 or model_of_your_car > 2021:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it...(◡‿◡✿)...")      
        
    # A def to ask about the color of car...
    def colors(self):
        color_of_your_car = int(input("Please enter the color of your car by number = 1 : Black , 2 : White , 3 : Red , 4 : Blue , 5 : Yellow > "))
        if color_of_your_car == 1:
            self.color = "Black"
        elif color_of_your_car == 2:
            self.color = "White"
        elif color_of_your_car == 3:
            self.color = "Red"
        elif color_of_your_car == 4:
            self.color = "Blue"
        elif color_of_your_car == 5:
            self.color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(✿◠‿◠)...") 
        while color_of_your_car != 1 and color_of_your_car != 2 and color_of_your_car != 3 and color_of_your_car != 4 and color_of_your_car != 5:
            color_of_your_car = int(input("Please enter the color of your car by number = 1 : Black , 2 : White , 3 : Red , 4 : Blue , 5 : Yellow > "))
            if color_of_your_car == 1:
                self.color = "Black"
            elif color_of_your_car == 2:
                self.color = "White"
            elif color_of_your_car == 3:
                self.color = "Red"
            elif color_of_your_car == 4:
                self.color = "Blue"
            elif color_of_your_car == 5:
                self.color = "Yellow" 
            else:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(✿◠‿◠)...") 

    # another def to ask about the color of seat cover...
    def seat_cover(self):
        color_of_seat_cover = int(input("Enter the color of seat cover by number please = 1 : Black , 2 : White , 3 : Black and white , 4 = Red , 5 : Yellow > "))
        if color_of_seat_cover == 1:
            self.seat_cover_color = "Black"
        elif color_of_seat_cover == 2:
            self.seat_cover_color = "White"
        elif color_of_seat_cover == 3:
            self.seat_cover_color = "Black/White"
        elif color_of_seat_cover == 4:
            self.seat_cover_color = "Red"
        elif color_of_seat_cover == 5:
            self.seat_cover_color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(∪ ◡ ∪)...")     
        while color_of_seat_cover!=1 and color_of_seat_cover!=2 and color_of_seat_cover!=3 and color_of_seat_cover!=4 and color_of_seat_cover!=5:
            color_of_seat_cover = int(input("Enter the color of set cover by number please = 1 : Black , 2 : White , 3 : Black and white , 4 = Red , 5 : Yellow > "))
        if color_of_seat_cover == 1:
            self.seat_cover_color = "Black"
        elif color_of_seat_cover == 2:
            self.seat_cover_color = "White"
        elif color_of_seat_cover == 3:
            self.seat_cover_color = "Black/White"
        elif color_of_seat_cover == 4:
            self.seat_cover_color = "Red"
        elif color_of_seat_cover == 5:
            self.seat_cover_color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(∪ ◡ ∪)...")

    
    #special options of BMW
    
    # A def of Massaging_Seats to ask if they want or not
    def Massaging_Seats(self):
        massaging_seats = int(input("Do you want the option of massaging seats ma'am/sir ? (1 : Yes , 2 : No ) > "))
        if massaging_seats == 1:
            self.massaging_seats = "Yes"
        elif massaging_seats == 2:
            self.massaging_seats = "No"
        else:
            print("You have entered a wrong number , please correct it...[^_^]...")
        while massaging_seats!=1 and massaging_seats!=2:
            massaging_seats = int(input("Do you want the option of massaging seats ma'am/sir ? (1 : Yes , 2 : No ) > "))
        if massaging_seats == 1:
            self.massaging_seats = "Yes"
        elif massaging_seats == 2:
            self.massaging_seats = "No"
        else:
            print("You have entered a wrong number , please correct it...[^_^]...")


    #Another def to see if they want Magic_Sky_Sunroof
    def Magic_Sky_Sunroof(self):
        magic_sky_sunroof = int(input("Do you want the option of magic sky sunroof ma'am/sir ? (1 : Yes , 2 : No) > "))
        if magic_sky_sunroof == 1:
            self.magic_sky_sunroof = "Yes"
        elif magic_sky_sunroof == 2:
            self.magic_sky_sunroof = "No"
        else:
            print("You have entered a wrong number , please correct it...[^*^]...")
        while magic_sky_sunroof!=1 and magic_sky_sunroof!=2:
            magic_sky_sunroof = int(input("Do you want the option of magic sky sunroof ma'am/sir ? (1 : Yes , 2 : No) > "))
        if magic_sky_sunroof == 1:
            self.magic_sky_sunroof = "Yes"
        elif magic_sky_sunroof == 2:
            self.magic_sky_sunroof = "No"
        else:
            print("You have entered a wrong number , please correct it...[^*^]...")

# Class number 2:
class Benz:

    # To calculate number of people who want to buy a car...
    Number_of_Buyers = 0
    
    # A def that included Name , ... of buyer...
    def __init__(self , Name , Last_name , Age , Id_number , Car):
 
        self.Name = Name
        self.Last_name = Last_name
        self.Age = Age
        self.Id_number = Id_number
        self.Car = Car
        Benz.Number_of_Buyers +=1 
        print(f"Hello mr/ms {Name} \n Based on Your choice , your car is {Car} , You have chosen a fast car , you won't regret...(◕‿-)...\n")


     # another def to ask about the model of car...
    def Model(self):
        model_of_your_car = int(input("Enter the model that you want please (from 2000 to 2021) > "))
        if model_of_your_car < 2000 or model_of_your_car > 2021:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it...(◡‿◡✿)...")
        while model_of_your_car<2000 or model_of_your_car>2021:
            model_of_your_car = int(input("Enter the model that you want please (from 2000 to 2021) > "))
            if model_of_your_car < 2000 or model_of_your_car > 2021:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it...(◡‿◡✿)...")
        self.model = model_of_your_car      

    # A def to ask about the color of car...
    def colors(self):
        color_of_your_car = int(input("Please enter the color of your car by number = 1 : Black , 2 : White , 3 : Red , 4 : Blue , 5 : Yellow > "))
        if color_of_your_car == 1:
            self.color = "Black"
        elif color_of_your_car == 2:
            self.color = "White"
        elif color_of_your_car == 3:
            self.color = "Red"
        elif color_of_your_car == 4:
            self.color = "Blue"
        elif color_of_your_car == 5:
            self.color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(✿◠‿◠)...") 
        while color_of_your_car != 1 and color_of_your_car != 2 and color_of_your_car != 3 and color_of_your_car != 4 and color_of_your_car != 5:
            color_of_your_car = int(input("Please enter the color of your car by number = 1 : Black , 2 : White , 3 : Red , 4 : Blue , 5 : Yellow > "))
            if color_of_your_car == 1:
                self.color = "Black"
            elif color_of_your_car == 2:
                self.color = "White"
            elif color_of_your_car == 3:
                self.color = "Red"
            elif color_of_your_car == 4:
                self.color = "Blue"
            elif color_of_your_car == 5:
                self.color = "Yellow" 
            else:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(✿◠‿◠)...") 
    # another def to ask about the color of seat cover...
    def seat_cover(self):
        color_of_seat_cover = int(input("Enter the color of seat cover by number please = 1 : Black , 2 : White , 3 : Black and white , 4 = Red , 5 : Yellow > "))
        if color_of_seat_cover == 1:
            self.seat_cover_color = "Black"
        elif color_of_seat_cover == 2:
            self.seat_cover_color = "White"
        elif color_of_seat_cover == 3:
            self.seat_cover_color = "Black/White"
        elif color_of_seat_cover == 4:
            self.seat_cover_color = "Red"
        elif color_of_seat_cover == 5:
            self.seat_cover_color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(∪ ◡ ∪)...")     
        while color_of_seat_cover!=1 and color_of_seat_cover!=2 and color_of_seat_cover!=3 and color_of_seat_cover!=4 and color_of_seat_cover!=5:
            color_of_seat_cover = int(input("Enter the color of seat cover by number please = 1 : Black , 2 : White , 3 : Black and white , 4 = Red , 5 : Yellow > "))
        if color_of_seat_cover == 1:
            self.seat_cover_color = "Black"
        elif color_of_seat_cover == 2:
            self.seat_cover_color = "White"
        elif color_of_seat_cover == 3:
            self.seat_cover_color = "Black/White"
        elif color_of_seat_cover == 4:
            self.seat_cover_color = "Red"
        elif color_of_seat_cover == 5:
            self.seat_cover_color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(∪ ◡ ∪)...") 
    
    # Special options

    # A def to contain special option of Nightvision_Dashboard_System
    def Nightvision_Dashboard_System(self):
        nightvision_dashboard_system = int(input("Do You want Nightvision_Dashboard_System ma'am/sir ? (1:Yes , 2:No) > "))
        if nightvision_dashboard_system == 1:
            self.nightvision_dashboard_system = "Yes"
        elif nightvision_dashboard_system == 2:
            self.nightvision_dashboard_system = "No "
        else:
            print("You have entered a wrong number , please correct it...(≧◡≦)...")
        while nightvision_dashboard_system!=1 and nightvision_dashboard_system!=2:  
            nightvision_dashboard_system = int(input("Do You want Nightvision_Dashboard_System ma'am/sir ? (1:Yes , 2:No) > "))
        if nightvision_dashboard_system == 1:
            self.nightvision_dashboard_system = "Yes"
        elif nightvision_dashboard_system == 2:
            self.nightvision_dashboard_system = "No "
        else:
            print("You have entered a wrong number , please correct it...(≧◡≦)...") 

    
    # Another def of special option of Starlight_Headliner
    def Starlight_Headliner(self):
        starlight_headliner = int(input("Do you want starlight_headliner ma'am/sir? (1:Yes , 2:No)"))
        if starlight_headliner == 1:
            self.starlight_headliner = "Yes"
        elif starlight_headliner == 2:
            self.starlight_headliner = "No"
        else:
            print("You have entered a wrong number , please correct it...{｡^◕‿◕^｡}...")   
        while starlight_headliner!=1 and starlight_headliner!=2:  
            starlight_headliner = int(input("Do you want starlight_headliner ma'am/sir? (1:Yes , 2:No)"))
        if starlight_headliner == 1:
            self.starlight_headliner = "Yes"
        elif starlight_headliner == 2:
            self.starlight_headliner = "No"
        else:
            print("You have entered a wrong number , please correct it...{｡^◕‿◕^｡}...")

#  Class number 3:

class Chevrolet:

    # To calculate number of people who want to buy a car...
    Number_of_Buyers = 0
    
    # A def that included Name , ... of buyer...
    def __init__(self , Name , Last_name , Age , Id_number , Car):
        # Put them in self. to make them unlocal
        self.Name = Name
        self.Last_name = Last_name
        self.Age = Age
        self.Id_number = Id_number
        self.Car = Car
        Chevrolet.Number_of_Buyers +=1 
        print(f"Hello mr/ms {Name} \n Based on Your choice , your car is {Car} , You have chosen a powerful car , you won't regret...(◕‿-)...\n")


     # another def to ask about the model of car...
    def Model(self):
        model_of_your_car = int(input("Enter the model that you want please (from 2000 to 2021) > "))
        if model_of_your_car < 2000 or model_of_your_car > 2021:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it...(◡‿◡✿)...")
        while model_of_your_car<2000 or model_of_your_car>2021:
            model_of_your_car = int(input("Enter the model that you want please (from 2000 to 2021) > "))
            if model_of_your_car < 2000 or model_of_your_car > 2021:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it...(◡‿◡✿)...")
        self.model = model_of_your_car      

    # A def to ask about the color of car...
    def colors(self):
        color_of_your_car = int(input("Please enter the color of your car by number = 1 : Black , 2 : White , 3 : Red , 4 : Blue , 5 : Yellow > "))
        if color_of_your_car == 1:
            self.color = "Black"
        elif color_of_your_car == 2:
            self.color = "White"
        elif color_of_your_car == 3:
            self.color = "Red"
        elif color_of_your_car == 4:
            self.color = "Blue"
        elif color_of_your_car == 5:
            self.color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(✿◠‿◠)...") 
        while color_of_your_car != 1 and color_of_your_car != 2 and color_of_your_car != 3 and color_of_your_car != 4 and color_of_your_car != 5:
            color_of_your_car = int(input("Please enter the color of your car by number = 1 : Black , 2 : White , 3 : Red , 4 : Blue , 5 : Yellow > "))
            if color_of_your_car == 1:
                self.color = "Black"
            elif color_of_your_car == 2:
                self.color = "White"
            elif color_of_your_car == 3:
                self.color = "Red"
            elif color_of_your_car == 4:
                self.color = "Blue"
            elif color_of_your_car == 5:
                self.color = "Yellow" 
            else:
                print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(✿◠‿◠)...")     

    # another def to ask about the color of seat cover...
    def seat_cover(self):
        color_of_seat_cover = int(input("Enter the color of seat cover by number please = 1 : Black , 2 : White , 3 : Black and white , 4 = Red , 5 : Yellow > "))
        if color_of_seat_cover == 1:
            self.seat_cover_color = "Black"
        elif color_of_seat_cover == 2:
            self.seat_cover_color = "White"
        elif color_of_seat_cover == 3:
            self.seat_cover_color = "Black/White"
        elif color_of_seat_cover == 4:
            self.seat_cover_color = "Red"
        elif color_of_seat_cover == 5:
            self.seat_cover_color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(∪ ◡ ∪)...")     
        while color_of_seat_cover!=1 and color_of_seat_cover!=2 and color_of_seat_cover!=3 and color_of_seat_cover!=4 and color_of_seat_cover!=5:
            color_of_seat_cover = int(input("Enter the color of set cover by number please = 1 : Black , 2 : White , 3 : Black and white , 4 = Red , 5 : Yellow > "))
        if color_of_seat_cover == 1:
            self.seat_cover_color = "Black"
        elif color_of_seat_cover == 2:
            self.seat_cover_color = "White"
        elif color_of_seat_cover == 3:
            self.seat_cover_color = "Black/White"
        elif color_of_seat_cover == 4:
            self.seat_cover_color = "Red"
        elif color_of_seat_cover == 5:
            self.seat_cover_color = "Yellow" 
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(∪ ◡ ∪)...")

    # special options of Chevrolet

    def Seat_Cover_Leather(self):
        seat_cover_leather = int(input("What kind of leather do you want for your car ma'am/sir ?(1 : Chevy tahoe , 2 : Chevy truck , 3 : Silverado 1500) > "))        
        if seat_cover_leather == 1:
            self.seat_cover_leather = "Chevy tahoe"
        elif seat_cover_leather == 2:
            self.seat_cover_leather = "Chevy truck"
        elif seat_cover_leather == 3:
            self.seat_cover_leather = "Silverado"    
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...◕‿ ◕...")  
        while seat_cover_leather!=1 and seat_cover_leather!=2 and seat_cover_leather!=3:          
            seat_cover_leather = int(input("What kind of leather do you want for your car ma'am/sir ?(1 : Chevy tahoe , 2 : Chevy truck , 3 : Silverado 1500) > "))        
        if seat_cover_leather == 1:
            self.seat_cover_leather = "Chevy tahoe"
        elif seat_cover_leather == 2:
            self.seat_cover_leather = "Chevy truck"
        elif seat_cover_leather == 3:
            self.seat_cover_leather = "Silverado"    
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...◕‿ ◕...")  

    def Dark_Window(self):
        dark_window = int(input("Do you want the option of dark window ma'am/sir? (1 : Yes , 2 : No) > "))
        if dark_window == 1:
            self.dark_window = "Yes"
        elif dark_window == 2:
            self.dark_window = "No"
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(¬‿¬)...")
        while dark_window!=1 and dark_window!=2:          
            dark_window = int(input("Do you want the option of dark window ma'am/sir? (1 : Yes , 2 : No) > "))
        if dark_window == 1:
            self.dark_window = "Yes"
        elif dark_window == 2:
            self.dark_window = "No"
        else:
            print("Sorry , There is a mistake with your number" , "\n", "Please correct it ...(¬‿¬)...")    


#Now the inputes should be entered here...
Buyer1 = BMW('John' , 'qiuzy' , 45 , 17365 , 'BMW')  
Buyer1.Model()
Buyer1.colors()
Buyer1.seat_cover()
Buyer1.Massaging_Seats()
Buyer1.Magic_Sky_Sunroof()
print(Buyer1.__dict__)
print(f"Number of Buyers from BMW company is {BMW.Number_of_Buyers}")

print( "\n" , "\n" )            

Buyer1 = Benz('Max' , 'wonder' , 32 , 14323 , 'Benz')
Buyer1.Model()
Buyer1.colors()
Buyer1.seat_cover()
Buyer1.Nightvision_Dashboard_System()
Buyer1.Starlight_Headliner()
print(Buyer1.__dict__)
print(f"Number of Buyers from Benz copany is {Benz.Number_of_Buyers}")

print( "\n" , "\n" )            

Buyer1 = Chevrolet('sara' , 'land' , 24 , 54132 , 'Chevrolet')
Buyer1.Model()
Buyer1.colors()
Buyer1.seat_cover()
Buyer1.Seat_Cover_Leather()
Buyer1.Dark_Window()
print(Buyer1.__dict__)
print(f"Number of Buyers from Chevrolet copany is {Chevrolet.Number_of_Buyers}")
