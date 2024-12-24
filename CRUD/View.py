from . import Operation

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