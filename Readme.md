# 📚 Library CLI App

**Library CLI App** is a simple Command Line Interface (CLI) application that allows users to manage book data with **CRUD** operations (Create, Read, Update, Delete). The data is stored in a plain text file (`data.txt`), and the project is designed with a modular approach using multiple Python files.

## 🎯 Key Features
- **Create**: Add new books to the list.  
- **Read**: Display all saved book data.  
- **Update**: Update information for a specific book.  
- **Delete**: Remove book data from the list.  

## 🛠️ Technologies Used
- **Programming Language**: Python  
- **Data Storage**: Plain text file (`data.txt`)  

## 📂 Project Structure
```
LIBRARY-APP/
│-- CRUD/
│   │-- __init__.py       # Package initialization
│   │-- Database.py       # Handles file read/write operations
│   │-- Operation.py      # CRUD operation logic
│   │-- Text.py           # CLI text and message templates
│   │-- Util.py           # Utility functions
│   │-- View.py           # Display formatted data to the user
│   │-- data.txt          # Storage for book data
│
│-- main.py               # Entry point of the application
```

### Structure Breakdown
- **main.py**: The main file that runs the application and controls the program flow.  
- **Database.py**: Manages reading from and writing to `data.txt`.  
- **Operation.py**: Contains the core logic for performing CRUD operations.  
- **Text.py**: Holds text messages and prompts used in the CLI interface.  
- **Util.py**: Provides helper functions to support the application.  
- **View.py**: Formats and displays data neatly to the user.  

## 💻 How to Run the Application
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd LIBRARY-APP
   ```
2. Run the main file:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to manage your library data.

## 🚀 Project Goals
This project was created to:
- Practice fundamental Python programming concepts.  
- Implement a modular code structure for better maintainability.  
- Learn how to read and write data using text files.  
- Build an interactive and user-friendly CLI application.

## 💡 Key Learnings
- Understanding **CRUD** operations in application development.  
- Organizing code into multiple modules/files.  
- File handling in Python using `open`, `read`, and `write`.  
- Designing a simple CLI-based interface.  

---