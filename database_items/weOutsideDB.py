# Author: Safia Shah
# Objective: This will create and update the current db
# last updated: Fri Jan 27 2023

import csv
import sqlite3 as lite
import os 
import sys
import pathlib
from os import system
import math


FILENAME = "weOrganized.csv"
DATABASE = "weOutside.db"
MENU = "Please enter a choice:\n1. Load CSV to DB\n2. Run SQL cmds\n3. Quit\n"
QUIT = 3

# Connect to database within this file. am not specifying a path so it results in this directory
conn = lite.connect(DATABASE)
cur = conn.cursor()

def weOutside()
    choice = ("Menu: \n1.Create a new table\n2.Insert Table values")
    
    # create a table


    #insert values
    with open(FILENAME) as file:
        rows = csv.reader(file)
        cur.executemany("INSERT into ")

    return

def readFile(fileName):
    # do the "other" option later
    db_choice = int(input("Which database are you entering into:\n 1. weOutside 2. other "))
    if db_choice == 1:
        weOutside() # enter in items from we outside db

    return

def sql_commands():
    return



def main():
    menuChoice = int(input(MENU))

    while menuChoice != QUIT:
        if menuChoice == 1:
            print("Reading the CSV file")
            readFile(FILENAME)
        elif menuChoice == 2:
            print("Running command script")
            sql_commands()
        else:
            print("please enter a valid choice of '1' , '2', or '3'")
        
        menuChoice = int(input(MENU)) # reprompt for no infinite loop :)

    if menuChoice == QUIT:
        #close connection and exit
        print("Exiting out of program and closing connection to database")
        conn.close()
        sys.exit()


main()



