# %%
import user
import add
import view
import remove
import amend
import checkout

# %%
def ask_user(shopping_cart_list):
    '''
    Ask user whether login or register
    then initiate login.py file
    '''
    choice1 = input("Are you a current user?(Y or N)")
    
    if choice1 == "Y" or choice1 == "y":
        a = user.login_user()
        if a == True:
            return menu(shopping_cart_list)
        
        elif a == False:
            choice2 = input("Do you want to register?(Y or N)")
            if choice2 == "Y" or "y":
                user.register()
                print("Please login now.")
                return ask_user(shopping_cart_list)
            elif choice2 == "N" or "n":
                return ask_user(shopping_cart_list)
            else:
                print("Please enter Y or N.")
                return ask_user(shopping_cart_list)

    
    elif choice1 == "N" or choice1 == 'n':
        choice3 = input("Do you want to register?(Y or N)")
        if choice3 == "Y" or choice3 =='y':
            user.register()
            print("Please login now.")
            return ask_user(shopping_cart_list)       
        elif choice3 == "N" or choice3 =='n':
            return ask_user(shopping_cart_list)
        else:
            print("Please enter Y or N.")
            return ask_user(shopping_cart_list)
    
    else:
        print("Please enter Y or N.")
        return ask_user(shopping_cart_list)

# %%

def menu(shopping_cart_list):
    '''
    List out different functions for user to choose
    Initiate corresponding py files
    '''
    user_command = input('''Please choose from the following:\n
                    [1] add item to shopping cart \n
                    [2] view shopping cart \n
                    [3] remove items \n
                    [4] amend item weight \n
                    [5] check-out ''')
    
    if user_command == '1':
        add.Add_items(shopping_cart_list)
        print("The item has been added to your shopping cart.")
        return menu(shopping_cart_list)
    
    elif user_command == '2':
        view.view_shopping_cart(shopping_cart_list)
        return menu(shopping_cart_list)
    
    elif user_command == '3':
        if shopping_cart_list == []:
            print ("Your shopping cart is empty.")
            return menu(shopping_cart_list)
        else:     
            remove.remove_item(shopping_cart_list)
            print("The item has been successfully removed.")
            return menu(shopping_cart_list)
    
    elif user_command == '4':
        if shopping_cart_list == []:
            print ("Your shopping cart is empty.")
            return menu(shopping_cart_list)
        else:
            amend.amend_item_weight(shopping_cart_list)
            print("Your item has been updated.")
            return menu(shopping_cart_list)
    
    elif user_command == '5':
        if shopping_cart_list == []:
            print ("Your shopping cart is empty.")
            return menu(shopping_cart_list)
        else:
            shopping_cart_dict = view.create_cart_dict(shopping_cart_list)
            checkout.check_out(shopping_cart_dict)
            checkout.save_to_sale_history(shopping_cart_dict)
            
            print("Invoice and stamps printed.")
            shopping_cart_list = []
            return menu(shopping_cart_list)
    
    else:
        print('Please enter "1","2","3","4" or "5"')
        return menu(shopping_cart_list)

# %%
shopping_cart_list = []   # Create an empty shopping cart
a = ask_user(shopping_cart_list)   # Start the program

