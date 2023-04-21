
import sqlite3

def create(file):
    conn=sqlite3.connect("towed-cars.db")
    cursor=conn.cursor()
    sql1="create table cars (tow_date int,make text,style text,model text,color text,plate text,state text,towed_to_address text)"
    cursor.execute(sql1)
    with open(file,'r') as f:
        for line in f:
            if not line.startswith("Tow Date"):
                info=line.split(",")
                date=info[0]
                make=str(info[1])
                style=str(info[2])
                model=str(info[3])
                color=str(info[4])
                plate=str(info[5])
                state=str(info[6])
                towed2=str(info[7])
                sql2="insert into cars (tow_date, make, style, model, color, plate, state, towed_to_address) values (:tow_date,:make,:style,:model,:color,:plate,:state,:towed_to_address)"
                cursor.execute(sql2,{"tow_date":date,"make":make,"style":style,"model":model,"color":color,"plate":plate,"state":state,"towed_to_address":towed2})
    
    conn.commit()
    conn.close()
           
def main():
    create("towed.csv")

main()
