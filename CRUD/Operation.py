from . import Database
from .Util import random_string
import time

# value mode:
# 'a' for append
# 'w' for write
def store(writer, title, year, mode='w'):
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["writer"] =  writer + Database.TEMPLATE["writer"][len(writer):]
    data["title"] =  title + Database.TEMPLATE["title"][len(title):]
    data["year"] =  year

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'

    try:
        with open(Database.DB_NAME,mode,encoding="utf-8") as file:
            file.write(data_str)
    except:
            print("Insert data failed.")

def create(writer, title, year):
    store(writer, title, year, "a")

def create_data():
    writer = input("Writer: ")
    title = input("Title: ")

    while(True):
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("field year must be integer, please insert again with format (yyyy)") 
        except:
            print("field year must be integer, please insert again with format (yyyy)")

    store(writer, title, year, "w")

def read():
        try:
            with open(Database.DB_NAME, "r") as file:
                 content = file.readlines()
                 return content
        except:
             print("failed to read database.")
             return False
        

    
    