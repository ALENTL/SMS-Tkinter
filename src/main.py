# Installing the modern tkinter module
from customtkinter import *
import mysql.connector as mc
from mysql_conf import Config

# Mysql connection
cnx = mc.connect(host="localhost", user=Config.user, password=Config.password, port=3306, database="SCHOOL")
cur = cnx.cursor()

# Just the basic main stuff part
if __name__ == "__main__":
    if cnx.is_connected():
        print("Connection successful")