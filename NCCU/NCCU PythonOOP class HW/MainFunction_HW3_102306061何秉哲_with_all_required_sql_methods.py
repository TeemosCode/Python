#102306061 資管三甲 何秉哲HW_3
#creates database with Interactive Create , Insert , Update , Delete and Query functions
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
    '''
    update = """UPDATE DMC_data
            SET ? = "?"
            WHERE ? = "?"
            """
    '''
    name = """UPDATE DMC_data
            SET NAME = ?
            WHERE NAME = ?
            """

    T97E = """UPDATE DMC_data
            SET TWD97_E = ?
            WHERE TWD97_E = ?
            """

    T97N = """UPDATE DMC_data
            SET TWD97_N = ?
            WHERE TWD97_N = ?
            """
    T97H = """UPDATE DMC_data
            SET TWD97_H = ?
            WHERE TWD97_H = ?
            """
    
    T67E = """UPDATE DMC_data
            SET TWD67_E = ?
            WHERE TWD67_E = ?
            """
    T67N = """UPDATE DMC_data
            SET TWD67_N = ?
            WHERE TWD67_N = ?
            """
    T67H = """UPDATE DMC_data
            SET TWD67_H = ?
            WHERE TWD67_H = ?
            """

    date = """UPDATE DMC_data
            SET DATE = ?
            WHERE DATE = ?
            """

    column = input("Which column to update?(NAME ,TWD97_E,TWD97_N,TWD97_H,TWD67_E,TWD67_N,TWD67_H,data)\n")
    set_data = input("Which data to update?\n")
    set_into = input("What changes would you like to make?\n")

    if column == "NAME":
        c.execute( name , (set_into , set_data) )
    elif column == "TWD97_E":
        c.execute( T97E , (set_into , set_data) )
    elif column == "TWD97_N":
        c.execute( T97N , (set_into , set_data) )
    elif column == "TWD97_H":
        c.execute( T97H , (set_into , set_data) )
    elif column == "TWD67_E":
        c.execute( T67E , (set_into , set_data) )
    elif column == "TWD67_N":
        c.execute( T67N , (set_into , set_data) )
    elif column == "TWD67_H":
        c.execute( T67H , (set_into , set_data) )
    elif column == "TWD67_H":
        c.execute( T67H , (set_into , set_data) )
    elif column == "DATE":
        c.execute( date , (set_into , set_data) )
    else:
        print("The column doesnt exist in this database!, Please try again!\n")
        Update()
        
#How to change columns with user input while using SQL syntax????
def Delete():
    '''
    delete = """
            DELETE FORM DMC_data
            WHERE ? = ?
            """
    '''
    name = """DELETE FROM DMC_data
            WHERE NAME = ?
            """
    T97E = """DELETE FROM DMC_data
            WHERE TWD97_E = ?
            """
    T97N = """DELETE FROM DMC_data
            WHERE TWD97_N = ?
            """
    T97H = """DELETE FROM DMC_data
            WHERE TWD97_H = ?
            """
    T67E = """DELETE FROM DMC_data
            WHERE TWD67_E = ?
            """
    T67N = """DELETE FROM DMC_data
            WHERE TWD67_N = ?
            """
    T67H = """DELETE FROM DMC_data
            WHERE TWD67_H = ?
            """
    date = """DELETE FROM DMC_data
            WHERE DATE = ?
            """
    delete = input("Which column data to delete?(NAME ,TWD97_E,TWD97_N,TWD97_H,TWD67_E,TWD67_N,TWD67_H,data)\n")
    data = input("Which data to delete?\n")


    if delete == "NAME":
        c.execute( name , [("%s")%data] )
    elif delete == "TWD97_E":
        c.execute( T97E , data )
    elif delete == "TWD97_N":
        c.execute( T97N , data )
    elif delete == "TWD97_H":
        c.execute( T97H , data )
    elif delete == "TWD67_E":
        c.execute( T67E , data )
    elif delete == "TWD67_N":
        c.execute( T67N , data )
    elif delete == "TWD67_H":
        c.execute( T67H , data )
    elif delete == "TWD67_H":
        c.execute( T67H , data )
    elif delete == "DATE":
        c.execute( date , data )
    else:
        print("The column doesnt exist in this database!, Please try again!\n")
        Delete()

def Query():
    query1 = """
         SELECT * FROM DMC_data
         WHERE ? = ?
         """
    query2 = """
         """


    name = """SELECT * FROM DMC_data
            WHERE NAME = ?
            """
    T97E = """SELECT * FROM DMC_data
            WHERE TWD97_E = ?
            """
    T97N = """SELECT * FROM DMC_data
            WHERE TWD97_N = ?
            """
    T97H = """SELECT * FROM DMC_data
            WHERE TWD97_H = ?
            """
    T67E = """SELECT * FROM DMC_data
            WHERE TWD67_E = ?
            """
    T67N = """SELECT * FROM DMC_data
            WHERE TWD67_N = ?
            """
    T67H = """SELECT * FROM DMC_data
            WHERE TWD67_H = ?
            """
    date = """SELECT * FROM DMC_data
            WHERE DATE = ?
            """
    
    query = input("Which specific column to choose from?(NAME ,TWD97_E,TWD97_N,TWD97_H,TWD67_E,TWD67_N,TWD67_H,DATE):\n")
    what = input("The data of your query in the column?:\n")

    
    if query == "NAME":
        c.execute( name , [("%s")%what] )
    elif query == "TWD97_E":
        c.execute( T97E , [("%s")%what])
    elif query == "TWD97_N":
        c.execute( T97N , [("%s")%what] )
    elif query == "TWD97_H":
        c.execute( T97H , [("%s")%what] )
    elif query == "TWD67_E":
        c.execute( T67E , [("%s")%what] )
    elif query == "TWD67_N":
        c.execute( T67N , [("%s")%what] )
    elif query == "TWD67_H":
        c.execute( T67H , [("%s")%what] )
    elif query == "TWD67_H":
        c.execute( T67H , [("%s")%what] )
    elif query == "DATE":
        c.execute( date , [("%s")%what] )
    else:
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

    

