#102306061 資管三甲 何秉哲HW_3
#testing easier syntax for SQL 
import sqlite3
db = open("SQLite_database" , mode = "r" , encoding = "UTF-8")
con = sqlite3.connect("database.db")
c = con.cursor()



create = """CREATE TABLE DMC_data
         (NAME text , TWD97_E text , TWD97_N text , TWD97_H text , TWD67_E text ,
         TWD67_N text , TWD67_H text , DATE text)
         """



def Create():
    c.execute(create)
    print("creating database...")
    for n in range(10):
        print(".....")
    print("Database created!!\n")

def Insert():
    lst = []
    s = 0
    for line in db:
        s += 1
        if s == 1:
            pass
        else:
            l = line.split()
            t = tuple(l)
            lst.append(t)

    c.executemany("INSERT INTO DMC_data VALUES (?,?,?,?,?,?,?,?)",lst)
    
#How to change columns with user input while using SQL syntax????



def Update():
    
    column = input("Which column to update?(NAME ,TWD97_E,TWD97_N,TWD97_H,TWD67_E,TWD67_N,TWD67_H,data)\n")
    
    update = """UPDATE DMC_data
            SET %s = ?
            WHERE %s = ?
            """%(column , column)
    
    set_data = input("Which data to update?\n")
    set_into = input("What changes would you like to make?\n")

    try:
        c.execute( update , (set_into , set_data) )
    except sqlite3.OperationalError:
        print("The column doesnt exist in this database!, Please try again!\n")
        Update()
    
#How to change columns with user input while using SQL syntax????
def Delete():
     
    delete = input("Which column data to delete?(NAME ,TWD97_E,TWD97_N,TWD97_H,TWD67_E,TWD67_N,TWD67_H,data)\n")

    d = """DELETE FROM DMC_data
            WHERE %s = ?
            """%delete
    
    data = input("Which data to delete?\n")


    try:
        c.execute( d, [("%s")%data] )
    except sqlite3.OperationalError:
        print("The column doesnt exist in this database!, Please try again!\n")
        Delete()

def Query(): 
    
    query = input("Which specific column to choose from?(NAME ,TWD97_E,TWD97_N,TWD97_H,TWD67_E,TWD67_N,TWD67_H,DATE):\n")

    q =  """
         SELECT * FROM DMC_data
         WHERE %s = ?
         """%query
    
    what = input("The data of your query in the column?:\n")

    
    try:
        c.execute( q , [("%s")%what])
    except sqlite3.OperationalError:
        print("The column doesnt exist in this database!, Please try again!\n")
        Query()
    
    print(c.fetchall())




if __name__ == "__main__":
    
    print("================DMC_data SQLite3 database=============")
    try:
        Create()
        Insert()
        con.commit()
    except sqlite3.OperationalError:
        print("DMC_data table 'already created'!\n")
    
    while True:
        p = input("What would you like to do with the database?( update(u) , query(q), delete(d) )\n"
                  +"(If you don't want to do anything to the database, enter 'n' or 'N') :\n")
        p = p.lower()
        if p == "update" or p == "u":
            Update()
            con.commit()
        elif p == "query" or p == "q":
            Query()
            con.commit()
        elif p == "delete" or p == "d":
            Delete()
            con.commit()
        elif p == 'n':
            break

    con.commit()
    db.close()
"""
def functionrun():
    print("================DMC_data SQLite3 database=============")
    try:
        Create()
        Insert()
        con.commit()
    except sqlite3.OperationalError:
        print("DMC_data table 'already created'!\n")
    
    while True:
        p = input("What would you like to do with the database?( update(u) , query(q), delete(d) )\n"
                  +"(If you don't want to do anything to the database, enter 'n' or 'N') :\n")
        p = p.lower()
        if p == "update" or p == "u":
            Update()
            con.commit()
        elif p == "query" or p == "q":
            Query()
            con.commit()
        elif p == "delete" or p == "d":
            Delete()
            con.commit()
        elif p == 'n':
            break

    con.commit()
    db.close()
    
"""

