# %%
import csv
from checkout import format_country_name

# %%
def Add_items (shopping_cart_list):
    '''
    Add a new string stating item details into the shopping_cart
    '''
    new_item_string = get_item_details()
    
    # check duplicate item in shopping cart
    if new_item_string in shopping_cart_list:
        choice = input('''There is one same item in the shopping cart, do you really want to add it?\n
              [1]Yes [2]No''')
        if choice.isdigit() == True and int(choice) == 1:
            shopping_cart_list.append(new_item_string)
            return (shopping_cart_list)
        elif choice.isdigit() == True and int(choice) == 2:
            return Add_items(shopping_cart_list)
        else:    
            print("Please enter 1 or 2")
            return Add_items(shopping_cart_list)
    
    # Add new item string to shopping cart
    else:
        shopping_cart_list.append(new_item_string)
        return(shopping_cart_list)
    
   

# %%
def get_country_zone_file():        
    '''
    Create a dictionary for Countries_and_Zones.csv file,
    with country name as keys, and corresponding zone as values
    '''
    country_zone_dict = {}
    
    with open('Countries_and_Zones.csv','r') as file:
        country_zone = csv.reader(file, delimiter = ',')
        for row in country_zone:
            # write each row into dictionary
            country_zone_dict[row[0]] = row[1]  
        return country_zone_dict

# %%
def check_zone():
    '''
    Ask user for destination country,
    then initiate get_country_file() function
    '''                    
    destination_country_input = input("Which country would you like to send to?")
    destination_country = format_country_name(destination_country_input)
    dic = get_country_zone_file()
    if destination_country in dic.keys():
        return (dic[destination_country],destination_country.upper())
    else:
        print ("Sorry, we do not send to this country.")
        return check_zone()

# %%
def get_stamp_price_letter_file():
    '''
    Create a nested dictionary for file Economy_Letter_Price_Guide.csv file,
    with weight as the first key and zone as the second key
    '''
    stamp_price_letter_dict = {}
    
    # Each row of the csv file turns into a list
    with open('Economy_Letter_Price_Guide.csv', 'r') as file:
        stamp_price_letter = csv.reader(file, delimiter=',')  
        
        # Create headers from the first row of the csv file
        zones_header = [zone for zone in next(stamp_price_letter)[1:]]

        for row in stamp_price_letter:
            stamp_price_letter_dict[row[0]] = dict(zip(zones_header, row[1:]))  # create a nested dictionary
        return stamp_price_letter_dict

# %%
def check_weight_letter():              
    '''
    Ask user for item weight,
    then find out the weight's category
    '''
    weight = input("What's the weight in kilogram?")
    
    if isfloat(weight) == False:
        print("Please enter numbers only")
        return check_weight_letter()
    elif isfloat(weight) == True:
        if float(weight) > 0 and float(weight) < 0.5 or float(weight) == 0.5:
            return ('Up to 500g',"%.4f"%float(weight))
        elif float(weight)>0.5 and float(weight) < 1.0 or float(weight) == 1.0:
            return ('Up to 1kg',"%.4f"%float(weight))
        elif float(weight)>1 and float(weight) < 1.5 or float(weight) == 1.5:
            return('Up to 1.5kg',"%.4f"%float(weight))
        elif float(weight)>1.5 and float(weight) < 2.0 or float(weight) == 2.0:
            return('Up to 2kg',"%.4f"%float(weight))
        else:
            print("Letter's weight can be up to 2kg")
            return check_weight_letter()
        

# %%
def isfloat(str):
    '''
    Check whether a string contains only floating point numbers
    '''             
    try:
        float(str)
        return True
    except ValueError:
        return False

# %%
def get_stamp_price_parcel_file():
    '''
    Create a nested dictionary for Economy_Parcel_Price_Guide.csv file,
    with weight as the first key and zone as the second key
    '''    
    stamp_price_parcel_dict = {}

    with open('Economy_Parcel_Price_Guide.csv', 'r') as file:
        stamp_price_parcel = csv.reader(file, delimiter=',')
        
        # Create headers from the first row of the csv file
        zones_header = [zone for zone in next(stamp_price_parcel)[1:]]
        for row in stamp_price_parcel:
            stamp_price_parcel_dict[row[0]] = dict(zip(zones_header, row[1:])) # create a nested dictionary
        return stamp_price_parcel_dict

# %%
def check_weight_parcel():
    '''
    Ask user for parcel's weight,
    then find out the weight's category
    '''           
    weight = input("What's the weight in kilogram?")
    if isfloat(weight) == False:
        print("Please enter numbers only")
    elif isfloat(weight) == True:
        if float(weight) < 2.5 or float(weight) == 2.5:
            print("Parcel's weight must be over 2.5kg.")
            return check_weight_parcel()
        elif float(weight) > 2.5 and float(weight) < 3.0 or float(weight) == 3.0:
            return ('Over 2.5 kg up to 3kg',"%.4f"%float(weight))
        elif float(weight)>3.0 and float(weight) < 5.0 or float(weight) == 5.0:
            return ('Up to 5kg',"%.4f"%float(weight))
        elif float(weight)>5.0 and float(weight) < 10.0 or float(weight) == 10.0:
            return ('Up to 10kg',"%.4f"%float(weight))
        elif float(weight)>10.0 and float(weight) < 15.0 or float(weight) == 15.0:
            return ('Up to 15kg',"%.4f"%float(weight))
        elif float(weight)>15.0 and float(weight) < 20.0 or float(weight) == 20.0:
            return ('Up to 20kg',"%.4f"%float(weight))
        else:
            print("The weight is too large. Seperate into small parcels if possible.")
            return check_weight_parcel()

# %%
def get_item_details():
    '''
    Ask for item details
    Return a string contains all item details
    '''
    
    post_type = input('''Please choose the type of the item you want to post:\n
                      [1]Letter  [2]Parcel''')
    
    # if the user selected option [1]
    if post_type.isdigit() == True and int(post_type) == 1:
        (zone_key,country) = check_zone()
        
        # Country entered not in the destination options
        if zone_key == None: 
            return get_item_details()
        else:
            (weight_key,weight) = check_weight_letter()
            
            # if weight entered not in range
            if weight_key == None: 
                return get_item_details()
            else:
                price_dict = get_stamp_price_letter_file()
                price_small = float(price_dict[weight_key][zone_key])
                price_medium = 1.1 * price_small   # increase 10% for medium letters
                price_large = 1.15 * price_small   # increase 15% for large letters
                letter_size = input('''What is the size of the letter?
                                    [1]Small  [2]Medium  [3]Large''')
                if letter_size.isdigit() == True and int(letter_size) == 1:  # Letter size is small
                    item_details_string = \
                        'Item type: letter(s)  Weight: {0:>7}kg  Destination: {1:<20} Unit price: $ {2:.2f}'\
                                                                    .format(weight,country,price_small)
                    return (item_details_string)
                
                elif letter_size.isdigit() == True and int(letter_size) == 2:  # Letter size is medium

                    item_details_string = \
                        'Item type: letter(m)  Weight: {0:>7}kg  Destination: {1:<20} Unit price: $ {2:.2f}'\
                                                                    .format(weight,country,price_medium)
                    return (item_details_string)
                
                elif letter_size.isdigit() == True and int(letter_size) == 3:  # Letter size is large

                    item_details_string = \
                        'Item type: letter(l)  Weight: {0:>7}kg  Destination: {1:<20} Unit price: $ {2:.2f}'\
                                                                    .format(weight,country,price_large)
                    return (item_details_string)
                
                else: 
                    print("Incorrect size, please start over.")  
                    return get_item_details()
                    
    # if the user selected option [2]                
    elif post_type.isdigit() == True and int(post_type) == 2: # User wants to post parcels
        (zone_key,country) = check_zone()  
        if zone_key == None: # country entered not in the destination options
            get_item_details()
        else:
            (weight_key,weight) = check_weight_parcel()
            
            # if weight entered not in range
            if weight_key == None: 
                get_item_details()
            else:
                price_dict = get_stamp_price_parcel_file()
                price_parcel = float(price_dict[weight_key][zone_key])

                item_details_string = \
                    'Item type: parcel(s)  Weight: {0:>7}kg  Destination: {1:<20} Unit price: $ {2:.2f}'\
                                                            .format(weight,country,price_parcel)
                return (item_details_string)
                
    
    else:
        print('Please enter "1" or "2"')
        return get_item_details()
                
        
        


