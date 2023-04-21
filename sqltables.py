
import sqlite3

def data(file,dbname):
    conn=sqlite3.connect(dbname)
    cursor=conn.cursor()
    sql1="create table sp_table (date text, open_price float, high_price float, low_price float, close_price float, volume int)"
    cursor.execute(sql1)
    with open(file, 'r') as f:
        for line in f:
            if not line.startswith("Date"):
                line=line.replace("\n","")
                l=line.split(",")
                date=l[0]
                open_price=float(l[1])
                high_price=float(l[2])
                low_price=float(l[3])
                close_price=float(l[4])
                volume=int(l[6])
                sql2="insert into sp_table (date,open_price,high_price,low_price,close_price,volume) values (:date,:open_price,:high_price,:low_price,:close_price,:volume)"

                cursor.execute(sql2,{"date":date,"open_price":open_price,"high_price":high_price,"low_price":low_price,"close_price":close_price,"volume":volume})
    conn.commit()
    conn.close()

def main():
    data("sandp.csv","sp.db")
    
    
main()
