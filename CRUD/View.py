from . import Operation

def update_console():
    read_console()
    
    while(True):
        print("Please insert book id")
        bookId = int(input("Book Id: "))
        record = Operation.read(index=bookId)

        if record:
            break
        else:
            print("book id not found, please insert again")
        
    # breakdown data
    data = record.split(",")
    pk          = data[0]
    createdAt   = data[1]
    writer      = data[2]
    title       = data[3]
    year        = data[4][:-1]

    while(True):
        print("\n"+"="*100)
        print("Please select data want updated")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Writer\t: {writer:.40}")
        print(f"3. Year\t: {year:40}")

        userOption = input("Select data [1,2,3]: ")
        print("\n"+"="*100)
        match userOption:
                case "1": title = input("title\t: ")
                case "2": title = input("writer\t: ")
                case "3": 
                    while(True):
                        try:
                            year = int(input("Year\t: "))
                            if len(str(year)) == 4:
                                break
                            else:
                                print("field year must be integer, please insert again with format (yyyy)") 
                        except:
                            print("field year must be integer, please insert again with format (yyyy)")
                case _: print("index don't match")
        is_done = input("Can be done update (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Operation.update(bookId,pk,createdAt,year,title,writer)

def create_console(): 
    print("\n\n"+"="*100)
    print("Please input book data\n")
    writer = input("Writer\t: ")
    title = input("Title\t: ")
    while(True):
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("field year must be integer, please insert again with format (yyyy)") 
        except:
            print("field year must be integer, please insert again with format (yyyy)")
        
    Operation.create(writer, title, year)
    print("Library list")
    read_console()

def read_console():
    data_file = Operation.read()
    index = "No"
    title = "Title"
    writer = "Writer"
    year = "Year"

    # Header    
    print("\n"+"="*100)
    print(f"{index:4} | {title:40} | {writer:40} | {year:5}")
    print("-"*100)

    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        writer = data_break[2]
        title = data_break[3]
        year = data_break[4]
        print(f"{index+1:4} | {title:.40} | {writer:.40} | {year:4}",end="")

    # Footer
    print("="*100+"\n")