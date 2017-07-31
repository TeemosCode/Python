# -*- coding: utf-8 -*-

"""
Sqllite
practice using sqlite3 module and SQL
changed old file database to sqlite database
also changed to string representations to practice using the 'str.format()' method instead of the '%' usage
"""

import os, sqlite3

#print(os.system("pwd"))
print()
print("Connecting to sqlite account database...")
print(".....")
print()

conn = sqlite3.connect("Account_Password.sqlite")
print("!!Connected to Account_Password.sqlite database!!")

#makes it easier to read in the terminal
def printline():
    print("=============================")
    print()

#program starting options
def menu():
	print('-------------------------------------------------')
	print('------- Password management File DataBase -------')
	print('1. Enter  Account  &  Password')
	print("2. Display  Account & Password")
	print("3. D e l e t e   A c c o u n t")
	print('4. U p d a t e        Password')
	print('0. Q  u  i  t          Program') 
	print('-------------------------------------------------')
    

#listing...
def accountExists(account):
    sqlread = "SELECT * FROM password WHERE name = '{}';".format(account)
    cursor = conn.execute(sqlread)
    datarow = cursor.fetchone()
    if datarow != None:
    	return True


def dataExists():
	sqlread = "SELECT * FROM password;"
	cursor = conn.execute(sqlread)
	datarow = cursor.fetchone()
	if datarow != None:
		return True

# saving in new account and password $$$$
def enter():
    
    while True:
        printline()
        account = input("Please Input Account (Quit by just pressing Enter button wihtout any inputs) --->  ")
        if account == '':
            break

        flag = accountExists(account)

        if flag:
        	print("Account '{}' already Exists! Please try again!".format(account))
        	continue

        print('Account : "{}" '.format(account)) 
        print("- - - - - - - - - - - - - - - - - ")
        password = input("Enter Password --->  ")
        while password == '' or ' ' in password:
            print("Password Length Must be OVER ONE nor can it contain spaces")
            printline()
            password = input("Enter Password --->  ")

        sqlGetPass='SELECT * FROM password WHERE password = "{}";'.format(password)
        cursor = conn.execute(sqlGetPass)
        print('password : {} '.format(len(password) * '*') )

        sqlSave = "INSERT INTO password VALUES('{}', '{}');".format(account, password)

        conn.execute(sqlSave)
        conn.commit()
            
        print("Account : {}, Password : {} SAVED!".format(account, (len(password)*'*') ))
        print("- - - - - - - - - - - - - - - - - ")

    
# Displaying Data
def display():
    sqlread = 'SELECT * FROM password;'
    cursor = conn.execute(sqlread)
    printline()
    print("===Account/tPassword===")
    print("---------------------------")
    print("Account\t\tPassword")
    print("---------------------------")
    for datarow in cursor:
    	print('{}\t\t{}'.format(datarow[0],datarow[1]))
    	print("- - - - - - - - - - - - - - - - - ")

#Deletion of 
def delete():
    while True:
        printline()

        flag = dataExists() 
        if not flag:
            print("No data in the file for deletion...")
            print("Please try another valid option")
            break
        print("----Existing Accounts----")
        display()
        todel = input("Which Account would you like to delete? (Press Enter without inputs to stop deletion progress)")
        
        if todel == '':
            break

        accntFlag = accountExists(todel)
        if not accntFlag:
            print('No Such account "{}" Exists! Please Try Again.'.format(todel))
            continue

        check = input("Are you sure you want to delete the Account '{}' ? ('Y or y' to delete) ".format(todel))
        print("- - - - - - - - - - - - - - - - - ")
        if check.lower() == 'y':
            sqlDel = 'DELETE FROM password WHERE name = "{}";'.format(todel)
            conn.execute(sqlDel)
            conn.commit()
            print("Deleted Account: '{}' from the database".format(todel))
            print("- - - - - - - - - - - - - - - - - ")
        
#the Update function   
def update():
    while True:
        printline()

        flag = dataExists()
        if not flag:
            print("No data in the file for update...")
            print("Please try another valid option")
            break
        print("----Existing Accounts----")
        display()
        toup = input("Which Account's password would you like to update? (Press Enter without inputs to stop Upgrade progress)")
        print("- - - - - - - - - - - - - - - - - ")
        if toup == '':
            break
        accntFlag = accountExists(toup)
        if not accntFlag:
            print("Account Doesn't Exist, please try again.")
            continue
        
        newpass = input("New Password ----> ")
        while newpass == '' or ' ' in newpass:
            print("Password must not contain spaces nor can its length be lesser than one")
            printline()
            newpass = input("New Password ----> ")
            print("- - - - - - - - - - - - - - - - - ")
        
        check = input("Are you sure to change password of Account '{}' ? ('Y or y' to delete)".format(toup))
        print("- - - - - - - - - - - - - - - - - ")
        if check.lower() == 'y':
            sqlUpdate = "UPDATE password SET password = '{}' WHERE name='{}';".format(newpass, toup)
            conn.execute(sqlUpdate)
            conn.commit()
            print("Password to Account: '{}' Updated!".format(toup))
            print("- - - - - - - - - - - - - - - - - ")
            
        
         
#Main program
if __name__ == "__main__":
    
    
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
            