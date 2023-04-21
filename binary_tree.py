class tree(object):
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None

    def gen(self,l):
        self.value=l[0]
        for value in l[1:]:
            self.insert(value)

    def insert(self,new_value):
        if new_value<=self.value:
            if self.left==None:
                self.left=tree(new_value)
            else:
                self.left.insert(new_value)
        else:
            if self.right==None:
                self.right=tree(new_value)
            else:
                self.right.insert(new_value)

    def post_trav(self):
        if self.left!=None:
            self.left.post_trav()
        if self.right!=None:
            self.right.post_trav()
        print(self.value)

    def leaf(self,c=0):
        if self.left==None and self.right==None:
            c+=1
        if self.left!=None:
            c+=self.left.leaf()
        if self.right!=None:
            c+=self.right.leaf()
        return c
        
def main():
    l=[6,3,0,5,1,8,9,7,10]
    T=tree()
    T.gen(l)
    print("Traverse LRW:")
    T.post_trav()
    print("Number of leaves:")
    print(T.leaf())
    
main()
   
