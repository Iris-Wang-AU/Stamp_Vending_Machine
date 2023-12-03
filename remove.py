# %%
def remove_item (shopping_cart_list):
    '''
    Remove an item from the shopping cart
    '''
    a1 = input("What is the number of the item that you want to remove?(numbers only)")
    
    if a1.isdigit() == True: 
        if int(a1) > 0 and int(a1) < len(shopping_cart_list) or int(a1) == len(shopping_cart_list):
            shopping_cart_list.pop(int(a1)-1)
            
        else:
            print("Item number out of range,please re-enter.")
            return remove_item(shopping_cart_list)
        
    else:
        print("Please enter a correct item number.")
        return remove_item (shopping_cart_list)


