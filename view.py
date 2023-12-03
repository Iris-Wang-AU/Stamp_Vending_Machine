# %%

def view_shopping_cart(shopping_cart_list):
    '''
    Show current items in the shopping cart with corresponding item numbers,
    and current items' total cost
    '''
    a1 = len(shopping_cart_list)
    if a1 == 0:
        print ("Your shopping cart is empty.")
    else:
        total_price = 0
        # get unit price in each item details
        for item in shopping_cart_list:
            n = item.find("$")+2
            price = item[n:]
            total_price += float(price)
        
        shopping_cart_dict = create_cart_dict(shopping_cart_list)
        
        for (a,b) in shopping_cart_dict.items():
            item_str = a + "  " + b
            print (item_str)    
        
        print( f"Total price: $ {total_price:.2f}" )
    
    

# %%
def create_cart_dict(shopping_cart_list):
    '''
    Create a dictionary,
    with item number as key,
    and item details as value
    '''
    a1 = len(shopping_cart_list)
    
    # Create a list for item numbers
    item_number_list = []
    for i in range(1,a1+1):
        item_number_list.append ("Item No: {}".format(i))
    
    # Join the item_number list and the item details list
    shopping_cart_dict = dict(zip(item_number_list,shopping_cart_list))
    return shopping_cart_dict
    


