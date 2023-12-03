# %%
def login_user():
    '''
    Ask for login details
    initiate check_password() function
    '''
    username = input("Please enter your username:").upper()
    password = input("please enter your password:")
    return check_password(username,password)

# %%
def check_password(username,password):
    '''
    Match login details with data stored
    Return True when match
    Return False when not
    '''
    password_dict = update_password_file()    
    
    if (username,password) in password_dict.items():  
        print("Hi "+ username +", you have successfully logged in.")
        return True
    else:
        print("Incorrect username or password.")         
        return False

# %%
def update_password_file():
    '''
    Create a dictionary for current usernames and passwords
    '''
    password_dict = {}
    try:
        with open("user_password.txt","r") as file: 
            for line in file:                   
                (ascii_key,ascii_value) = line.strip().split(",")           
                (username,password) = decrypt_ascii(ascii_key,ascii_value) 
                password_dict[username] = password 
    
    # If any unneccessary new lines or spaces inserted to the user_password.txt file
    except ValueError:    
        print('''
            Check user_password.txt file
            Extra space or new line included
            Please restore the file to last saved version
          ''')
    return (password_dict)

# %%
def encrypt_ascii (username,password):
    '''
    Encode username and password using ASCII value
    Ciper-text = character + 12 (student ID % 128)
    '''  
    encrypted_username = ""
    for a in username:
        encrypted_username += chr(ord(a)+12)
        
    encrypted_password = ""
    for b in password:
        encrypted_password += chr(ord(b)+12)
    
    return(encrypted_username,encrypted_password)

# %%
def decrypt_ascii (encrypted_username,encrypted_password):  
    '''
    Decode encrypted username and password
    Plain text = character - 12 (student ID % 128)
    '''
    username = ""
    for a in encrypted_username:
        username += chr(ord(a)-12)
    
    password = ""
    for b in encrypted_password:
        password += chr(ord(b)-12)
    
    return (username,password)

# %%
def register():
    '''
    Register a new user
    Save new username and password to user_password.txt file
    '''
 
    password_dict = update_password_file()
    
    username = input("Please create your username (must be 8 alphabets)").upper()
    if len(username) != 8 or username.isalpha () == False:    
        print("Username must be 8 alphabets, re-register please.") 
        # Take user back to re-register
        return register()          
    else:                                                    
        # Check the existance of the username.
        if username in password_dict.keys():                  
            print("Username already existed, please create a new one.")
            return register()
        else:   
            password = input("Please create your password(must be 4 digits):")
            if len(password) !=4 or password.isdigit() == False:    
                print("Password must be 4 digits, re-register please.")
                return register()

            else:
                print("Hi "+ username +", You have successfully registered, now back to login menu.")
                # Save new username and password to user_password.txt file
                with open ("user_password.txt","a") as file:        
                    (ascii_key,ascii_value) = encrypt_ascii(username,password)
                    file.write(ascii_key+","+ascii_value+"\n")
   


