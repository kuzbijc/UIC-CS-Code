import sqlite3

def db_and_table():
    conn = sqlite3.connect("mydata.db") # establishing connection
    cursor = conn.cursor() # allows you to browse tables
    sql1 = "create table students (name text, username text, id int)" # table contains... ()
    cursor.execute(sql1) # execute..
    cursor.close() # done
        
def add_data(): # what you will see when you run this file in ubuntu
    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()
    print("Input Student Data: ")
    while True:
        name = input("Student's Name: ")
        username = input("Student's Username: ")
        ID = int(input("Student's ID: "))
        sql2 = "insert into students (name, username, ID) values (:name, :username, :ID)"
        cursor.execute(sql2,{"name":name, "username":username, "ID":ID})
        conn.commit() # updating data
        loopcontrol = input("Add another student? (yes or no)")
        if loopcontrol == 'n':
            break
    cursor.close()
        
def fetch_db_data():
    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()
    sql3 = "select * from students"
    results = cursor.execute(sql3)
    all_students = results.fetchall() # python command, creates list
    for student in all_students:
        print(student)
    
def main():
    db_and_table()
    add_data()
    fetch_db_data()

main()
