# %%
import csv
from add import get_country_zone_file
from add import get_stamp_price_letter_file
from add import get_stamp_price_parcel_file
from add import isfloat

# %%
def amend_item_weight(shopping_cart_list):
    '''
    Ask for new item weight
    then create a new string contains new item details,
    and update the old item to new item in the shopping cart
    '''
    a1 = input("What is the number of the item that you want to amend?(numbers only)")
    if a1.isdigit() == True: 
            if int(a1) > 0 and int(a1) < len(shopping_cart_list) or int(a1) == len(shopping_cart_list) :
                item = shopping_cart_list[int(a1)-1]
                item_type = item[11:20]
                item_country = item[54:74].strip()
                new_weight = input("What is the new weight in kilogram?")
                new_price = get_new_price(item_type,item_country,new_weight)
                if new_price == None:
                    print("Please start over.")
                    return amend_item_weight(shopping_cart_list)
                else:
                    new_weight_format = "%.4f"%float(new_weight)                
                    shopping_cart_list[int(a1)-1] = 'Item type: {0}  Weight: {1:>7}kg  Destination: {2:<20} Unit price: $ {3:.2f}'\
                                                            .format(item_type,new_weight_format,item_country,new_price)
            
            else:
                print("Please enter a correct number.")
                return amend_item_weight(shopping_cart_list)
                                                                   
    else:
        print("Please enter a correct number.")
        return amend_item_weight(shopping_cart_list)
                
    

# %%
def get_zone(country):
    '''
    Formating the country name, ie UNITED STATES to United States
    '''             
    country_zone_dict = get_country_zone_file()
    if country.count(" ") == 0: # Country name contains only 1 word like "China"
        country_key = country.capitalize()
        zone = country_zone_dict[country_key]
        return zone
    elif country.count(" ") == 1: # Country name contains 2 words like "United States"
        (x,y) = country.split()
        country_key = x.capitalize()+" "+y.capitalize()
        zone = country_zone_dict[country_key]
        return zone
    elif country.count(" ") == 2: # Country name contains 3 words like "Papua New Guinea"
        (x,y,z) = country.split()
        country_key = x.capitalize()+" "+y.capitalize()+" "+z.capitalize()
        zone = country_zone_dict[country_key]
        return zone

# %%
def get_weight(weight):
    '''
    Look up the item's weight catogery
    '''                    
    a = float(weight)
    if a < 0.5 or a == 0.5:
        weight_key = "Up to 500g"
        return weight_key
    elif a > 0.5 and a < 1.0 or a == 1.0:
        weight_key = "Up to 1kg"
        return weight_key
    elif a > 1.0 and a < 1.5 or a == 1.5:
        weight_key = "Up to 1.5kg"
        return weight_key
    elif a > 1.5 and a < 2.0 or a == 2.0:
        weight_key = "Up to 2kg"
        return weight_key
    elif a > 2.5 and a < 3.0 or a == 3.0:
        weight_key = "Over 2.5 kg up to 3kg"
        return weight_key
    elif a > 3.0 and a < 5.0 or a == 5.0:
        weight_key = "Up to 5kg"
        return weight_key
    elif a > 5.0 and a < 10.0 or a == 10.0:
        weight_key = "Up to 10kg"
        return weight_key
    elif a > 10.0 and a < 15.0 or a == 15.0:
        weight_key = "Up to 15kg"
        return weight_key
    elif a > 15.0 and a < 20.0 or a == 20.0:
        weight_key = "Up to 20kg"
        return weight_key    

# %%
def get_new_price(item_type,item_country,new_weight):
    '''
    Get new price for new weight by 
    searching Economy_Letter_Price_Guide file and Economy_Parcel_Price_Guide file
    '''
    # For small parcel:
    if item_type == "parcel(s)":
        if isfloat(new_weight) == True:
            if float(new_weight) > 2.5 and float(new_weight) < 20 or float(new_weight) == 20:
                price_dict = get_stamp_price_parcel_file()
                new_price = price_dict[get_weight(new_weight)][get_zone(item_country)]
                return float(new_price)
            else:
                print("Letter weight must be over 0kg and up to 2kg")
                
        elif isfloat(new_weight) == False:
            print("Please enter only numbers.")
            
    # For small letter:
    elif item_type == "letter(s)":
        if isfloat(new_weight) == True:
            if float(new_weight) > 0 and float(new_weight) < 2.0 or float(new_weight) == 2.0:
                price_dict = get_stamp_price_letter_file()
                new_price = price_dict[get_weight(new_weight)][get_zone(item_country)]
                return float(new_price)
            else:
                print("Letter weight must be over 0kg and up to 2kg")
                
        elif isfloat(new_weight) == False:
            print("Please enter only number.")
            
    # For medium letter:
    elif item_type == "letter(m)":
        if isfloat(new_weight) == True:
            if float(new_weight) > 0 and float(new_weight) < 2.0 or float(new_weight) == 2.0:
                price_dict = get_stamp_price_letter_file()
                new_price_small = price_dict[get_weight(new_weight)][get_zone(item_country)]
                new_price = float(new_price_small) * 1.1  # increase price by 10% for medium letters
                return float(new_price)
            else:
                print("Letter weight must be over 0kg and up to 2kg")
                
        elif isfloat(new_weight) == False:
            print("Please enter only number.")
            
    # For large letter:
    elif item_type == "letter(l)":
        if isfloat(new_weight) == True:
            if float(new_weight) > 0 and float(new_weight) < 2.0 or float(new_weight) == 2.0:
                price_dict = get_stamp_price_letter_file()
                new_price_small = price_dict[get_weight(new_weight)][get_zone(item_country)]
                new_price = float(new_price_small) * 1.15 # increase price by 15% for large letters
                return float(new_price)
            else:
                print("Letter weight must be over 0kg and up to 2kg")
                
        elif isfloat(new_weight) == False:
            print("Please enter only number.")
            
    


