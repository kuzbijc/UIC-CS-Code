"""
w for write
r for read
a for append
a+ for read and append
r+ for read and write
"""

def opening_file(s):
    l = []
    with open(s, 'r') as f:
        for lines in f:
            lines = lines.replace("\n","")
            lines = lines.split(",")
            name = lines[0]
            email = lines[-1]
            username = email.split("@")
            username = username[0]
            l.append([name, email, username])
    return l
           
def write2file(file,I):      
    cnt = 1
    with open(file,'w') as f:
        for info in I:
            name = info[0]
            email = info[1]
            username = info[2]
            f.write("%s. %s, %s, %s \n" % (str(cnt),name,email,username))
            cnt += 1

def main():
    I = opening_file("mathdepartment.txt") # name, email, username
    write2file("output.txt",I)

main()
