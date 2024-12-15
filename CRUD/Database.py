from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXX",
    "date_add": "yyyy-mm-dd",
    "title":255*" ",
    "writer":255*" ",
    "title":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database is found, app is ready")
    except:
        print("Database not found, please create a new database")
        with open(DB_NAME, "w", encoding="utf-8") as file:
            Operation.create_data()
        