import os
import CRUD as CRUD

if __name__ == "__main__":
    operating_system = os.name # find os type

    # Infinite loop, for make sure app don't stopped
    while(True):

        # Clear console
        match operating_system:
            case "posix" : os.system("clear")
            case "nt": os.system("cls")

        # Print welcome text
        print("WELCOME")
        print("LIBRARY DATABASE")
        print("=========================")
        
        # print option list
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        # user input
        user_option = input("Enter opsi: ")

        print("\n=========================\n")

        # find match user input
        match user_option:
            case "1" : print("Read Data")
            case "2" : print("Create Data")
            case "3" : print("Update Data")
            case "3" : print("Delete Data")

        print("\n=========================\n") 

        # answer
        is_done = input("Can be done (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

        print("App is stopped, thank you.")
            
    