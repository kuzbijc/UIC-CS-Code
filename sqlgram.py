"""
Write a Python/SQLite function that creates a database with a table called
n-grams, which consists of three columns of type text, called 1-gram, 2-gram,
3-gram. A n-gram is formed in the following way. Consider a sentence "today is
a nice day." A 1-gram would be a column consisting of [today, is, a, nice, day].
A 2-gram would be [today is, is a, a nice, nice day]. A 3-gram would be
[today is a, is a nice, a nice day]. You can use the Chicago Wikipedia
article (Lecture 5) to build these n-grams.
"""
import sqlite3

def create(text):
    conn=sqlite3.connect("gram.db")
    cursor=conn.cursor()
    sql1="create table grams (one text, two text, three text)"
    cursor.execute(sql1)
    l=[]
    with open(text,'r') as f:
        for line in f:
            l=line.split(" ")
            one=[]
            two=[]
            three=[]
            for i in range(len(l)): # 1gram
                s=""
                for j in range(1):
                    s+=l[i+j] + " "
                one.append(s[: -1])
            for i in range(len(l)-1): # 2gram
                s=""
                for j in range(2):
                    s+=l[i+j] + " "
                two.append(s[: -1])
            for i in range(len(l)-2): # 3gram
                s=""
                for j in range(3):
                    s+=l[i+j] + " "
                three.append(s[: -1])
            one=str(one)
            two=str(two)
            three=str(three)
            sql2="insert into grams (one,two,three) values (:one,:two,:three)"
            cursor.execute(sql2,{"one":one,"two":two,"three":three})
    conn.commit()
    conn.close()        
            
            
            
            
def main():
    create("chicago-wikipedia-article.txt")


main()
