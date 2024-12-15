from . import Database
from .Util import random_string
import time

def create_data():
    writer = input("Writer: ")
    title = input("Title: ")
    year = input("Year: ")

    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["writer"] =  writer + Database.TEMPLATE["writer"][len(writer):]
    data["title"] =  title + Database.TEMPLATE["title"][len(title):]
    data["year"] =  year

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'
   
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
            print("Insert data failed.")

def read():
        try:
            with open(Database.DB_NAME, "r") as file:
                 content = file.readlines()
                 return content
        except:
             print("failed to read database.")
             return False
        

    
    