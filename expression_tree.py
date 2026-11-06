"""#  File: ExpressionTree.py

#  Description: The expression will be a valid infix expression with the
#  all the necessary parentheses so that there is no ambiguity
#in the order of the expression. 

#  Student Name: Mia Garza

#  Student UT EID: mkg2545

#  Course Name: CS 313E

#  Unique Number: 54970

#  Date Created: 11/4

#  Date Last Modified: 11/6
"""
import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack ():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0



class Node ():
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild



class Tree():
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        tokens=expr.split()
        stack=Stack()

        self.root=Node()
        cur_node=self.root

    #determining the type of the token
        for token in tokens:
            if token=="(":
                cur_node.lChild=Node()
                stack.push(cur_node)
                cur_node=cur_node.lChild

            elif token in operators:
                cur_node.data=token
                stack.push(cur_node)
                cur_node.rChild=Node()
                cur_node=cur_node.rChild

            elif token ==")":
                if not stack.is_empty():
                    cur_node=stack.pop()

            else:
                cur_node.data=token
                cur_node=stack.pop()

    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.lChild is None and aNode.rChild is None:
            return float(aNode.data)

        left=self.evaluate(aNode.lChild)
        right=self.evaluate(aNode.rChild)
        operator=aNode.data

        #calculating the operators manually  
        # + - * / // % **
        if operator=="+":
            return left+right

        elif operator=="-":
            return left-right

        elif operator=="*":
            return left*right

        elif operator=="/":
            return left/right

        elif operator=="//":
            return left//right

        elif operator=="%":
            return left%right

        elif operator=="**":
            return left**right

    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if aNode is None:
            return ""
        return aNode.data+ " "+ self.pre_order(aNode.lChild)+ self.pre_order(aNode.rChild)
        

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if aNode is None:
            return ""
        return self.post_order(aNode.lChild) + self.post_order(aNode.rChild) + aNode.data + " "




# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
