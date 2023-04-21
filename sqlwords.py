"""
Write a Python/SQLite function that creates a database with a table
called article, which consists of 3 columns: word (type text), word
length (type int), word frequency (type int). Use the Chicago Wikipedia
article (Lecture 5) for this problem. After you have created the database,
pass this database to Python/SQLite functions that can return average word
length, maximal word length, minimal word length, and most frequent word
from the database table.
"""

import sqlite3

def create(text):
    conn=sqlite3.connect('word.db')
    cursor=conn.cursor()
    sql1="create table info (word text, length text, freq text)"
    cursor.execute(sql1)
    with open(text,'r') as f:
        for words in f:
            l1=words.split(" ")
            print(l1)
            l2=[len(words) for words in l1]
            print(l2)
            l3=[l1.count(words) for words in l1]
            print(l3)
            l1=str(l1)
            l2=str(l2)
            l3=str(l3)
            sql2="insert into info (word,length,freq) values (:word,:length,:freq)"
            cursor.execute(sql2,{"word":l1,"length":l2,"freq":l3})
            conn.commit()
    conn.close()
         
    
def main():
    create("chicago.txt")

main()
