# Installing the modern tkinter module
from customtkinter import CTk
import mysql.connector as mc
from mysql_conf import Config

# Mysql connection
cnx = mc.connect(host="localhost", user=Config.user, password=Config.password, port=Config.port, database="SCHOOL")
cur = cnx.cursor()

# SQL Connection check
def sql_check():
    if cnx.is_connected() == True:
        print("Database connection established")
        return True

# Default run command
def run():
    a = sql_check()
    if a == True:
        window = CTk()
        window.mainloop()


# Just the basic main stuff part
if __name__ == "__main__":
    run()