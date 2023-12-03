# %%
import datetime
import csv
from csv import writer

# %%
def get_final_sale_id():
    '''
    Get the last sale id from sales_history.csv file
    '''
    with open('sales_history.csv', 'r') as file:
        final_row = file.readlines()[-1]
        final_sale_id = int(final_row.split(",")[0])
        return final_sale_id

# %%
def get_size(item_str):
    '''
    Get item's size from shopping cart details
    '''
    item_type = item_str[11:20]
    if item_type == "parcel(s)":
        return "small"
    elif item_type == "letter(s)":
        return "small"
    elif item_type == "letter(m)":
        return "medium"
    elif item_type == "letter(l)":
        return "large"

# %%
def check_out(shopping_cart_dict):
    '''
    Save and display invoice with a list of all items
    and each individual stamp
    '''
    invoice_title = '{}.txt'.format(datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S'))
    with open (invoice_title,'x') as file:
        
        invoice_header = "--------------Invoice---------------"
        invoice_end = "------------End Invoice--------------"
        
        file.write(invoice_header +"\n")
        print(invoice_header +"\n")
        
        # join two lists together
        invoice_item_list = list(zip(shopping_cart_dict.keys(),shopping_cart_dict.values()))
        
        # write each item details into invoice file
        for n in invoice_item_list:
            file.write((str(n).replace(","," ").replace("(","",1).replace("'",""))[:-1]+"\n")
            print((str(n).replace(","," ").replace("(","",1).replace("'",""))[:-1]+"\n")
        
        # calculate total price
        total_price = 0
        for (item_no,item_str) in invoice_item_list:
            n = item_str.find("$")+2
            item_price = item_str[n:]
            total_price += float(item_price)
        
        # write the total cost into invoice file
        file.write("\n"+"Total Cost: $ "+str("%.2f"%total_price)+"\n"+invoice_end+"\n")
        print("\n"+"Total Cost: $ "+str("%.2f"%total_price)+"\n"+invoice_end+"\n")
        
        # write each stamps into invoice file
        stamps_header = "-----------Purchased Stamps-------"
        stamps_end =    "----------------------------------"
        for item_str in shopping_cart_dict.values():
            item_type = item_str[11:20]
            item_country = item_str[41:74].strip()
            item_weight = item_str[22:35]+"kg"
            file.write("\n"+ stamps_header+"\n" \
                            +item_type+"\n" \
                            +item_country+"   "+item_weight +"\n" \
                            +stamps_end +"\n")

            print("\n"+ stamps_header+"\n" \
                            +item_type+"\n" \
                            +item_country+"   "+item_weight +"\n" \
                            +stamps_end +"\n")
            

# %%
def save_to_sale_history(shopping_cart_dict):
    '''
    Save current sale to sales_history.csv file
    '''
    new_sale_id = get_final_sale_id() + 1
    shopping_cart_list = shopping_cart_dict.values()
    
    # Create a list containing all item details
    new_sales_list = []
    for item in shopping_cart_list:
        sale_id = new_sale_id
        date_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
        item_type = item[11:17]
        weight = item[29:35]
        country = item[54:74].strip()
        country_name = format_country_name(country)
        size = get_size(item)
        cost = float(item[89:])
        new_sales_item = [sale_id,date_time,item_type,weight,country_name,size,cost]
        new_sales_list.append(new_sales_item)
    
    # add new sale details into sales_history.csv file
    with open('sales_history.csv', 'a', newline='') as f:
        w = writer(f)
        w.writerows(new_sales_list)
        

    

# %%
def format_country_name(country):
    '''
    Format country names ie. UNITED STATES to United States 
    '''
    a1 = country.find(" ")
    if a1 == -1: # country name contains only 1 word, like "China"
        country_name = country.capitalize()
    else: # country name contains more than one wor, like "United States"
        country_name_list = country.split()
        country_name = ""
        for c in country_name_list:
            country_name += c.capitalize() + " "
    return country_name.strip()


