import os
operations = ["help", "create table", "run"]
def add_to_file(source, text):
    with open(source, "r") as read:
        lines = read.readlines()
    lines.append(text)
    with open(source, "w") as write:
        for line in lines:
            write.write(line + "\n")
user = input("Please enter your MySQL username: ")
password = input("Please enter your MySQL password: ")
database = input("Please enter the database to use: ")
add_to_file("to_do.sql", "USE " + database + ";")
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
            table_name = input("What do you want to name this table? \n")
            table_values = input("What values (collums) do you want for you table? Please use commas between values. \n")
            add_to_file("to_do.sql", "CREATE TABLE " + table_name + " (" + table_values + ");")
        elif do == "run":
            os.system("mysql -u " + user + " -p " + password + " < to_do.sql")


