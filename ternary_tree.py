
class tree(object):
    def __init__(self,number=None):
        self.number=number
        self.left=None
        self.middle=None
        self.right=None

    def gen(self,l):
        self.number=l[0]
        for num in l[1:]:
            self.insert(num)

    def insert(self,num):
        if num<self.number:
            if self.left==None:
                self.left=tree(num)
            else:
                self.left.insert(num)
        elif num==self.number:
            if self.middle==None:
                self.middle=tree(num)
            else:
                self.middle.insert(num)
        else:
            if self.right==None:
                self.right=tree(num)
            else:
                self.right.insert(num)

    def trav(self):
        if self.left!=None:
            self.left.trav()
        if self.middle!=None:
            self.middle.trav()
        if self.right!=None:
            self.right.trav()
        print(self.number)

    def leaf(self,c=0):
        if self.left==None and self.middle==None and self.right==None:
            c+=1
        if self.left!=None:
            c+=self.left.leaf()
        if self.middle!=None:
            c+=self.middle.leaf()
        if self.right!=None:
            c+=self.right.leaf()
        return c
         
def main():
    l=[4,1,2,2,3,1,0,4,6,5,6,4]
    T=tree()
    T.gen(l)
    print("Traverse LMRW:")
    T.trav()
    print("Number of leaves:")
    print(T.leaf())

main()
