Active_User_List = []
try: 
      with open('Active_Users.txt', 'r') as file:
         for Act_User_List in file:
            Active_User_List.append(Act_User_List.strip())
except FileNotFoundError:
          print("Active users list not found")
def save_Active_Users(Active_User_List):
     #save Added user back to Active_users.txt file
     try:
        with open('Active_Users.txt','w') as file:
             for User in Active_User_List:
                  file.write(User + '\n')
     except: Exception as e:
        print (f"Error saving products: {e}")

def save_products(Active_User_List):
    #Save products back to Products.txt file
    try:
        with open('Products.txt', 'w') as file:
            for product in products:
                file.write(product + '\n')
    except Exception as e:
        print(f"Error saving products: {e}")


Disabled_User_List =[]
try:
      with open('Disabled_User_List.txt', 'r') as file:
                for Dis_User_List in file:
                     Disabled_User_List.append(Act_User_List.strip())
except FileNotFoundError:
      print("Disabled user list not found")

def save_Disabled_Users(Disabled_User_List):
     #save Added user back to Active_users.txt file
     try:
        with open('Disabled_Users.txt','w') as file
             for User in Dis_User_List:
                  file.write(User + '\n')
     except: Exception as e:
        print (f"Error saving products: {e}")

def print_Type_of_user():
     print("1. Active User")
     print("Disabled User")


def print_main_menu():
    print( "Main Menu")
    print("1. Add User")
    print("2. View Active/Disabled Users")
    print("3. Enable/Disable User")
    print("0. Exit")

while True:
     
  print_main_menu
  User_input = int(input("plese input the index of your chouce"))

  if User_input == 0:
       print ("exiting app, Thank you for using the app")
       print("User list has been updated")
       save_Active_Users
       save_Disabled_Users
       break

        
  elif User_input == 1:
     while True:  
        print_Type_of_user
        User_type_choice = input('please choose the type of user you want to add')
        while True
            if User_type_choice == 1:
                
                    New_Active_User = input("input the new active user")
                    if New_Active_User in Active_User_List:
                        print ("This user already exists")
                    else:
                        Active_User_List.append(New_Active_User)
            elif User_type_choice == 2:
                    New_Disabled_User = input ("please input new disabled user")
                    if New_Disabled_User in Disabled_User_List:
                        print ("This disabled user already exists")
                    else:
                        Disabled_User_List.append(New_Disabled_User)
            else :
                 print ("please enter a valid input")

  elif User_input == 2:
       print (f"the Active Users are \n{Active_User_List}")
       print (f"the Disabled users are \n {Disabled_User_List}")

  elif User_input == 3:
       while True:
            print_Type_of_user
            User_choice = input ("please select the choice to view active or disabled list")
            if user_input_3 == 1:
                 print("please select the index of the user you want to disable")
                 

       
       






            
        
              

