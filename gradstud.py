
import sqlite3

def create_db(file):
    conn=sqlite3.connect("mydb.db")
    cursor=conn.cursor()
    sql1="create table stat (name text,email text)"
    sql2="create table pm (name text,email text)"
    sql3="create table am (name text,email text)"
    sql4="create table cs (name text,email text)"
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    l2=[]
    with open(file,'r') as f:
        for line in f:
            l=line.replace("\t"," ")
            l=l.split(" ")
            email=l[-1]
            major=l[-2]
            name=" ".join(l[:-2])
            l2.append([name,major,email])
        for e in l2:
            if e[1]=="STAT":
                sql5="insert into stat (name,email) values (:name,:email)"
                cursor.execute(sql5, {"name":name,"email":email})
            elif e[1]=="PM":
                sql6="insert into pm (name,email) values (:name,:email)"
                cursor.execute(sql6, {"name":name,"email":email})
            elif e[1]=="AM":
                sql7="insert into am (name,email) values (:name,:email)"
                cursor.execute(sql7, {"name":name,"email":email})
            else:
                sql8="insert into cs (name,email) values (:name,:email)"
                cursor.execute(sql8, {"name":name,"email":email})
    conn.commit()
    conn.close()
    
def main():
    create_db("grad.txt")

main()
