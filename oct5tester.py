




# class Node():

#     def __init__(self,key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def print_node(self, level=0):
#         if self.rChild != None:
#             self.rChild.print_node(level + 1)

#         print(' ' * 4 * level + '->', self.key)

#         if self.lChild != None:
#             self.lChild.print_node(level + 1)


#     def in_order_traversal(self,aNode):
#         if aNode != None:
#             aNode.in_order_traversal(self.lchild)
#             print(aNode.key, end=" ")
#             aNode.in_order_traversal(self.rchild)

#     def pre_order_traversal(self,aNode):
#         if aNode != None:
#             print(aNode.key, end=" ")
#             aNode.pre_order_traversal(self.lchild)
#             aNode.pre_order_traversal(self.rchild)


#     def post_order_traversal(self,aNode):
#         if aNode != None:
#             aNode.pre_order_traversal(self.lchild)
#             aNode.pre_order_traversal(self.rchild)
#             print(aNode.key, end=" ")


# class BST():
#     def __init__(self):
#         self.root=None

#     def print(self,lvl):
#         self.root.print_node(lvl)

#     def insert(self):




#last class


# class Node():

#     def __init__(self, key):
#         self.key=key
#         self.lchild= None
#         self.rchild=None


#     def depth(node):
#         if node is None:
#             return 0
#         return 1+ max(depth(node.lchild), depth(node.rchild))



# class Node():

#     def __init__(self, key):
#         self.key=key
#         self.lchild= None
#         self.rchild=None


#     def inordertrav(self, aNode):
#         if aNode != None:
#             aNode.inordertrav(self.lchild)
#             print(aNode.key, end=" ")
#             aNode.inordertrav(self.rchild)

#     def preordertrav(self, aNode):
#         if aNode!=None:
#             print(aNode.key, end=" ")
#             aNode.inordertrav(self.lchild)
#             aNode.inordertrav(self.rchild)


#     def postorder(self, aNode):
#         aNode.inordertrav(self.lchild)
#         aNode.inordertrav(self.rchild)
#         print(aNode.key, end=" ")













"""
pre-order:
1) visit root
2) left child and descendants as a subtree and traverse it
3) repeat with right child

#41 is a subtree, so take it into consideration. take it all the way into leaf node




###output
60, 41, 16, 25, 53, 46, 42, 55, 74, 65,63,62,64,70



#in order
keep on going left anf left and further left and down. if furthest node doenst have anything below it
go back up one

16, 25, 41, 42, 46, 53, 55, 60, 62, 63, 64, 65, 70, 74


#post order

25, 16, 42, 46, 55, 53,  41, 62,64, 63,70, 65, 74, 60
"""



# def print_num_pattern(num1, num2):
#     print(num1, end=" ")
#     if num1<0:
#         return 
#     print_num_pattern(num1-num2, num2)
#     print(num1, end=" ")
    
#     #return print_num_pattern(num1+num2, num2)

# if __name__ == "__main__":
#     num1 = int(input())
#     num2 = int(input())
#     print_num_pattern(num1, num2)





# class Node():
#     def __init__(self, data, next_link=None):
#         self.data= data
#         self.link= next_link


# class LinkedList():
#     def __init__(self):
#         self.first=None

#     def insert_first(self,data):
#         new_link=Node(data) #create a known object to make linkedlist, builingblock, create node object
#         new_link.link= self.first
#         self.first=new_link #reassigning it to the front after youve created it 


# #remove current last link
# #make last element go to none
# #remove the link of 30 to None, and 40's link should go to None
#     def insert_last(self,data):
#         new_link=Node(data)
#         #start from the beginning and go to the end
#         current=self.first

#         if current is None:
#             self.first=new_link
#         while current.link is not None:
#             current=current.link
#         current.next=new_link


#     def __str__(self):
#         return str(self.first)

    
# def main():
#     ll=LinkedList()

#     ll.insert_first(10)
#     print(ll)
#     ll.insert_first(20)
#     print(ll)


# if __name__=='__main__':
#     main()



# class Node:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node
            
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         if not self.head:
#             self.head = Node(data)
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = Node(data)





# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def calculate_pay(self):
#         pass

#     def employee_type(self):
#         return "Employee"

#     def describe(self):
#         return f"{self.employee_type()} {self.name}: {self.calculate_pay()}"


# class SalariedEmployee(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary

#     def calculate_pay(self):
#         return self.salary // 12

#     def employee_type(self):
#         return "Salaried employee"


# class HourlyEmployee(SalariedEmployee):
#     def __init__(self, name, salary, hours, rate):
#         super().__init__(name, salary)
#         self.hours = hours
#         self.rate = rate

#     def calculate_pay(self):
#         return self.hours * self.rate

#     def employee_type(self):
#         return "Hourly employee"


# class Intern(HourlyEmployee):
#     def __init__(self, name, salary, hours, rate):
#         super().__init__(name, salary, hours, rate)

#     def calculate_pay(self):
#         # call the Employee method
#         return Employee.calculate_pay(self)

#     def employee_type(self):
#         return "Intern"


# def main():
#     employees = [
#         SalariedEmployee("Aziz", 72000),
#         HourlyEmployee("Aadil", 36000, 75, 3),
#         Intern("Keshika", 12000, 40, 5)
#     ]

#     for employee in employees:
#         print(employee.describe())


# if __name__ == "__main__":
#     main()