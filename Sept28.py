
# class Stack():
#     def __init__(self):
#         self.stack=[]

#     def push(self,item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()

#     def is_empty(self):
#         return len(self.stack)==0

#     def peek(self):
#         return self.stack[len(self.stack)-1]

#     def __str__(self):
#         return str(self.stack)

# myStack =Stack()
# #push items
# myStack.push(10)
# myStack.push(20)
# print(myStack.peek())
# print(myStack.pop())
# print(myStack)

    


# def permutation(lst, start,end):
#     if start==end:
#         print(lst)
#     else:
#         for i in range(start,end+1):
#             #choose
#             lst[start],lst[i]=lst[i],lst[start]
#             #exploration
#             permutation(lst,start+1,end)
#             #unchoose
#             lst[start],lst[i]= lst[i], lst[start]

# permutation(["B", "E", "V"],0,2)




# print("week 6")


# def numSum(n):
#     if n==0:    #could also be 0 
#         return 0
#     else:
#         return numSum(n-1)+ n   #addition could be either way 

# #print(numSum(5))



# def pow(base, exponent):
#     if exponent==1:
#         return base
#     else:
#         return base*pow(base,exponent-1)

# # print(pow(3,4))
# # print(pow(2,2))
# # print(pow(3,1))


# def fibo(num):
#     if num==0:
#         return 0
#     if num==1:
#         return 1
#     else:
#         return fibo(num-1)+fibo(num-2)

# print(fibo(6))

# 0 1 1 2 3 5 8 13
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

print(fib(8))

"""
fib(8)
returns 7+6, 
returns 6+5
returns 5+4.....
returns 4+3 
returns 3+2



"""

# n = 3
"""


n = 4

((((


"""

# def parentheses(n):