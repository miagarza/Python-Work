#  File: TestBinaryTree.py

#  Description: performing methods on binary trees

#  Student Name: Mia Garza

#  Student UT EID: mkg2545


#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified: Oct 22


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


    def print_node(self, level=0):

        if self.lchild != None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild != None:
            self.rchild.print_node(level + 1)


    def get_height(self):
        if self.lchild != None and self.rchild != None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        elif self.lchild != None:
            return 1 + self.lchild.get_height()
        elif self.rchild != None:
            return 1 + self.rchild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lchild
                else:
                    curr = curr.rchild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node
            return





    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):

        if self.root is None:
            return "Range Undefined"

        if self.root==1:
            return 1

        current=self.root
        while current.lchild is not None:
            current=current.lchild
        mini=current.data 


        current=self.root
        while current.rchild is not None:
            current=current.rchild
        maxi=current.data

        return maxi-mini



    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):

        if self.root is None:
            return []

        currentlvl=[self.root]
        for i in range(level):
            next=[]
            for node in currentlvl:
                if node.lchild is not None:
                    next.append(node.lchild)
                if node.rchild is not None:
                    next.append(node.rchild)
            currentlvl=next
        return currentlvl


        
   


    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        if self.root is None:
            return []

        result=[]
        leftlist=[self.root]

        while len(leftlist)>0:
            result.append(leftlist[0].data)
            next=[]
            for node in leftlist:
                if node.lchild is not None:
                    next.append(node.lchild)
                if node.rchild is not None:
                    next.append(node.rchild)
            leftlist = next
        return result



    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        
        if self.root is None:
            return 0

        total=0
        nodes=[self.root]

        while len(nodes)>0:
            current=nodes.pop()
            if current.lchild is None and current.rchild is None:
                total+=current.data
            else:
                if current.lchild is not None:
                    nodes.append(current.lchild) 
                #sum1+=current.data
                if current.rchild is not None:
                    nodes.append(current.rchild)

        return total
        

def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree



# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.
if __name__ == '__main__':
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print('Tree range is: ',   t1.range())
    print('Tree left side view is: ', t1.left_side_view())
    print('Sum of leaf nodes is: ', t1.sum_leaf_nodes())
    print('##########################')

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print('Tree range is: ',   t2.range())
    print('Tree left side view is: ', t2.left_side_view())
    print('Sum of leaf nodes is: ', t2.sum_leaf_nodes())
    print('##########################')
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print('Tree range is: ',   t3.range())
    print('Tree left side view is: ', t3.left_side_view())
    print('Sum of leaf nodes is: ', t3.sum_leaf_nodes())
    print('##########################')