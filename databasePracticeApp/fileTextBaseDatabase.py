# -*- coding: utf-8 -*-

"""
file text-based database --- ver1
"""

import os
import os.path, ast

#print(os.system("pwd"))
print()
print()

#makes it easier to read in the terminal
def printline():
    print("=============================")
    print()

#program starting options
def menu():
    print('------- Password management File DataBase -------')
    print('1. Enter  Account  &  Password')
    print("2. Display  Account & Password")
    print("3. D e l e t e   A c c o u n t")
    print('4. U p d a t e        Password')
    print('0. Q  u  i  t          Program') 
    print('-------------------------------------------------')
    

# Reading the file that serves as a database (Like a database connection)
def read():
    with open("passwordFileDatabase.txt", 'r', encoding = 'UTF-8') as file:
        f = file.read()
        if f != '':
            data = ast.literal_eval(f)  # evaluates string literals (text files) that are dict format into python dictionary data structure 
            return data
        else:
            return {}


# saving in new account and password $$$$
def enter():
    printline()
    while True:
        
        account = input("Please Input Account (Quit by just pressing Enter button wihtout any inputs) --->  ")
        if account == '':
            break
        if account in data:
            print( 'Account "%s" already exists! Please try again!' % account)
            continue
        print('Account : "%s" ' % account) 
        print('-------    -------')
        password = input("Enter Password --->  ")
        while password == '' or ' ' in password:
            print("Password Length Must be OVER ONE nor can it contain spaces")
            printline()
            password = input("Enter Password --->  ")
        
        print('password : %s '% (len(password) * '*') ) 
        
        
        data[account] = password
        with open("passwordFileDatabase.txt", 'w', encoding = 'UTF-8') as file:
            file.write(str(data))
            
        print("Account : %s, Password : %s  SAVED!" % (account, (len(password)*'*') ))

    
# Displaying Data
def display():
    printline()
    print("===Account/tPassword===")
    print("---------------------------")
    for key in data:
        print("{}/t{}".format(key, data[key]))
        print("- - - - - - - - - - - - - - - - - ")
    
    #input("Press Enter Key to Return To Option Menu")
    

#Deletion of 
def delete():
    while True:
        
        if data == {}:
            printline()
            print("No data in the file for deletion...")
            print("Please try another valid option")
            break
        print("----Existing Accounts----")
        display()
        todel = input("Which Account would you like to delete? (Press Enter without inputs to stop deletion progress)")
        
        if todel == '':
            break
        if todel not in data:
            print('Account "%s" may already Exist or No Such account Exists! Please Try Again.' % todel)
            continue
        
        check = input("Are you sure you want to delete the Account '%s' ? ('Y or y' to delete) " % todel)
        if check.lower() == 'y':
            del data[todel]
            with open("passwordFileDatabase.txt", 'w' , encoding = "utf-8") as file:
                file.write(str(data))
        
#the Update function   
def update():
    while True:
        
        if data == {}:
            printline()
            print("No data in the file for update...")
            print("Please try another valid option")
            break
        print("----Existing Accounts----")
        display()
        toup = input("Which Account's password would you like to update? (Press Enter without inputs to stop Upgrade progress)")
        
        if toup == '':
            break
        if toup not in data:
            print("Account Doesn't Exist, please try again.")
            continue
        
        newpass = input("New Password ----> ")
        while newpass == '' or ' ' in newpass:
            print("Password must not contain spaces nor can its length be lesser than one")
            printline()
            newpass = input("New Password ----> ")
        
        check = input("Are you sure to change password of Account '%s' ? ('Y or y' to delete)" % toup)
        if check.lower() == 'y':
            data[toup] = newpass
            with open("passwordFileDatabase.txt", 'w', encoding = 'utf-8') as file:
                file.write(str(data))
         
#Main program
if __name__ == "__main__":
    #the global varibable, 'data' for user to tinker around with the read data
    data = read()
    while True:
        menu()
        todo = input("What would you like to do?")
        printline()
        if todo not in '01234':
            print("Sorry, no Corresponding Actions to such option, please try again!")
            printline()
            continue
        elif todo == '0':
            print("System shutting down ...")
            for i in range(3):
                print('...')
            print("System successfully Shut Down")
            break
        elif todo == '1':
            enter()
        elif todo == '2':
            display()
        elif todo == '3':
            delete()
        elif todo == '4':
            update()
            