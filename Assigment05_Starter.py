# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Natalie P,8/82023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# File to List
try:
    objFile = open(objFile, "r") # read in the data from the text file
    for row in objFile: # to loop through the rows of data
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow) # add the rows to the table in a list
        print (lstTable)
    objFile.close()
except:
    print("No file yet")
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for row in lstTable: # go through the list table
            print(row) # show the current data
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        Task = input("Enter an Task: ") # add a new task
        Priority = input("Enter a Priority: ") # add the priority level
        dicRow = {"Task":Task, "Priority":Priority} # row of data
        lstTable.append (dicRow) # each dicRow is part of a table data
        print (lstTable) # see the newest addition to the table list
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # slicing the list
        lstTable= lstTable[:-1]
        # print the updated list
        print("New list: ",lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"] +'\n'))
        objFile.close()
        print('Data was saved')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Exiting Program')
        break  # and Exit the program
    print('please choose from the options from 1 to 5')
