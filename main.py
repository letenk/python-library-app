import os
import CRUD as CRUD
import CRUD.Text as text

if __name__ == "__main__":
    operating_system = os.name # find os type

    # Clear console
    match operating_system:
        case "posix" : os.system("clear")
        case "nt": os.system("cls")
    
    text.welcome_text()

    CRUD.init_console()

    # Infinite loop, for make sure app don't stopped
    while(True):

        # Clear console
        match operating_system:
            case "posix" : os.system("clear")
            case "nt": os.system("cls")

        # Print welcome text
        text.welcome_text()
        
        # print option list
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        # user input
        user_option = input("Enter opsi: ")

        # find match user input
        match user_option:
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : print("Update Data")
            case "3" : print("Delete Data")

        # answer
        is_done = input("Can be done (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

        print("App is stopped, thank you.")
            
    