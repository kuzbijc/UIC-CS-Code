
import sqlite3

def create():
    conn=sqlite3.connect("mydb.db")
    cursor=conn.cursor()
    sql1="create table speed_vio (address text, cameraid text, day int, month int, year int, violations int)"
    cursor.execute(sql1)
    cursor.close()

def add_data():
    conn=sqlite3.connect("mydb.db")
    cursor=conn.cursor()
    
    with open("speed.csv",'r') as f:
        for line in f:
            if not line.startswith("ADDRESS"):
                L=line.split(",")
                address=L[0]
                cameraid=L[1]
                date=L[2].split("/")
                month=int(date[0])
                day=int(date[1])
                year=int(date[2])
                vio=int(L[3])
                sql2="insert into speed_vio (address,cameraid,day,month,year,violations) values (:address,:cameraid,:day,:month,:year,:violations)" 
                cursor.execute(sql2,{"address":address,"cameraid":cameraid,"day":day,"month":month,"year":year,"violations":vio})
                conn.commit()
                
    cursor.close()

def display_all():
    conn=sqlite3.connect("mydb.db")
    cursor=conn.cursor()
    sql3="select * from speed_vio"
    columns=cursor.execute(sql3)
    all_entries=columns.fetchall()
    for entry in all_entries:
        print(entry)

def display_address():
    conn=sqlite3.connect("mydb.db")
    cursor=conn.cursor()
    sql4="select address from speed violation"
    ad_columns=cursor.execute(sql3)
    all_addresses=ad_columns.fetchall()
    for address in all_addresses:
        print(address)

def display_other():
    conn=sqlite3.connect("mydb.db")
    cursor=conn.cursor()
    sql5="select min(violations) from speed violation"
    sql6="select max(violations) from speed violation"
    sql7="select sum(violations) from speed violation"
    minn=cursor.execute(sql5).fetchone()[0]
    maxx=cursor.execute(sql6).fetchone()[0]
    summ=cursor.execute(sql7).fetchone()[0]
    print(minn,maxx,summ)
              
def main():
    create()
    add_data()
    display_all()
    display_address()
    display_other()

main()
