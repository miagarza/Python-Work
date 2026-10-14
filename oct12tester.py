


class Node():

    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        if self.rchild != None:
            self.rchild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.key)

        if self.lchild != None:
            self.lchild.print_node(level + 1)


    def in_order_traversal(self,aNode):
        if aNode != None:
            aNode.in_order_traversal(aNode.lchild)
            print(aNode.key, end=" ")
            self.in_order_traversal(aNode.rchild)

    def pre_order_traversal(self,aNode):
        if aNode != None:
            print(aNode.key, end=" ")
            self.pre_order_traversal(aNode.lchild)
            self.pre_order_traversal(aNode.rchild)


    def post_order_traversal(self,aNode):
        if aNode != None:
            aNode.pre_order_traversal(aNode.lchild)
            aNode.pre_order_traversal(aNode.rchild)
            print(aNode.key, end=" ")


class BST():
    def __init__(self):
        self.root=None

    def print(self,lvl):
        self.root.print_node(lvl)

    def insert(self, value):
        new_node=Node(value)

        if self.root== None:
            self.root=new_node
        else:
            current=self.root
            parent=self.root

        #searching for location to find the tree node
            while(current != None):
                parent= current

                if (value< current.key):
                    current = current.lchild #if its less, then go left
                else:
                    current=current.rchild  #if its more, then go right

        #insert the node in that specific location
            if (value < parent.key):
                parent.lchild=new_node
            else:
                parent.rchild=new_node

    def delete(self, key):
        current=self.node
        parent= None
        isLeft= False

        #search for the node to be deleted
        while current is not None and current.key != key:
            parent=current

            if key<current.key:
                current=current.lchild
                isLeft=True
            else:
                current=current.rchild
                isLeft=False

        deleteNode=current

        #if empty tree or key not found
        if deleteNode==None:
            return False

        #case1 leaf node, you would figure this out by determining if the current node is Null
        if deleteNode.lchild==None and deleteNode.rchild==None:
            if deleteNode==self.root:
                self.root=None
            elif isLeft:
                parent.lchild=None
            else:
                parent.rchild=None

        #only left child
        elif deleteNode.rchild==None: 
            if deleteNode ==self.root:
                self.root= deleteNode.lchild
            elif isLeft:
                parent.lchild=deleteNode.lchild
            else:
                parent.rchild=deleteNode.lchild

        #only right child
        elif deleteNode.lchild==None:
            if deleteNode==self.root:
                self.root=deleteNode.rchild
            elif isLeft:
                parent.lchild= deleteNode.rchild
            else:
                parent.lchild=deleteNode.rchild

        #two children
        

        
            







#######working on this part 
    # def treesearch(x,k):
    #     if x==None or k==x.current:
    #         return x.current

    #     if k< x.current:
    #         return treesearch(x.lchild, k)
    #     else:
    #         return treesearch(x.rchild, k)
        


def main():
    bst=BST()

    bst.insert(10)
    bst.insert(19)
    bst.insert(5)
    bst.insert(44)
    bst.insert(84)
    bst.insert(64)
    bst.insert(77)
    bst.insert(92)
    bst.print(2)

    #test out pre-order, in-order, post-order code
    bst.root.in_order_traversal(bst.root)
    print()
    bst.root.pre_order_traversal(bst.root)
    print()
    bst.root.in_order_traversal(bst.root)


main()