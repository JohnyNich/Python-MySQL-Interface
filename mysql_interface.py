import os
import sys
operations = ["help", "create table", "run", "quit", "add data"]
source = "to_do.sql" # I'm using a variable as it will save time
def add_to_file(source, text):
    with open(source, "r") as read:
        lines = read.readlines()
    lines.append(text + "\n")
    with open(source, "w") as write:
        for line in lines:
            write.write(line)
user = input("Please enter your MySQL username: ")
database = input("Please enter the database to use: ")
with open(source, "w") as write:
    write.write("# This is where all the SQL commands go \n") # This is so that everytime the document opens, the previous is cleared
add_to_file(source, "USE " + database + ";")
ready = False

while ready == False:
    do = input("What do you want to do? \n")
    do = do.lower()
    if do not in operations:
        print("Sorry, you can't do that. Type help to show allowed commands. \n")
    else:
        if do == "help":
            print(operations)
        elif do == "create table":
            values = {}
            values_list = []
            done = False
            table_name = input("What do you want to name this table? \n")
            print("What values (columns) do you want for you table? Enter each value's name and type.")
            while done != True:
                value = input("What is the name of this value? \n")
                value = value.lower()
                value_type = input("What type is this? \n")
                value_type = value_type.upper()
                while value_type != "TEXT" and value_type != "INTEGER":
                    value_type = input("That's not a registered value type. Please enter either text or integer as a value type. \n")
                    value_type = value_type.upper()
                values[value] = value_type
                done = input("Do you want to add in any other values?\n")
                done = done.lower()
                while done != "yes" and done != "no":
                    done = input("Please enter either yes or no\n")
                    done = done.lower()
                if done == "no":
                    done = True # No need for an else statment, because done would still not be equal to True, so the loop would continue.
            for value in values:
                values_list.append(value + " " + values[value])
            values = ", ".join(values_list)
            print(values)
            add_to_file(source, "CREATE TABLE " + table_name + " (" + values + ");")
        elif do == "run":
            os.system("mysql -u " + user + " -p < to_do.sql")
        elif do == 'add data': # Note: Work in progress
            table = input("Which table do you want to add")
            value_orders = input("What is the order of values?")
            values = input("What are the values? Enter these with a comma in between each value")
            add_to_file(source, "INSERT INTO " + table + " (" + value_orders + ") VALUES (" + values + ");")
        elif do == "quit":
            sys.exit()


