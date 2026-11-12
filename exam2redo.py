#exam 2 redo
#question one

class Node:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def max_depth_stack(root=0):
        if root is None:
            return 0

"""both stacks are empty, need to put the root 
into the node stack and its corresponding 
depth into the depth stack  """      
        nodes=[]    #nodes=[root]
        depths=[]   #depths=[0] 

        new_node=Node(value)

        if self.root==None:
            depths.push(0)
        else:
            current=self.root
            count=0

        while current != None:
            parent=current

            {{{{if value<current.key:
                count+=1
                current=current.lchild
            else:
                count+=1
                current=current.rchild}}}}

        depths.push(count)
        ex=depths.peek()
        max=0

        if ex>max:
            max=ex
        else:
            max=max


            