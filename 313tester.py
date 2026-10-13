



# Return True if s is a palindrome.
# Case-insensitive. Letters only,
# no spaces or punctuation.
# "abcbba" -> False
# "Racecar" -> True
def isPalindrome(s: str) -> bool:
    s=s.lower()
    l, r = 0, len(s)
    print(f"debugging: {l}, {r}")
    while l <= r:
        if s[l] != s[r-1]:
            return False
        l += 1
        r -= 1
    return True

isPalindrome("abcbba")
isPalindrome("racecar")

# def exception_handler(op, val):
#     try:
#         if op == "divide":
#             return 10 // val
#         elif op == "lookup":
#             my_dict = {"a": 1, "b": 2}
#             return my_dict[val]
#         elif op == "list":
#             my_list = [1, 2, 3]
#             return my_list[val]
#         else:
#             return 10 + val
        
#         except ZeroDivisionError:
#             print("Caught ZeroDivisionError")
#             return None
#         except KeyError:
#             print("Caught KeyError")
#             return -1
#         except IndexError:
#             print("Caught IndexError")
#             return -2
#         except TypeError:
#             print("Caught TypeError")
#             return -3
#         finally:
#             print("Input: ", val





# try:
#     file=open("aug31.pdf","r")
#     data=file.read()
#     print(data)
#     file.close()
# except FileNotFoundError:
#     print("file not found")
# finally:
#     print("\n will always run!!! \n")
#     if file is not None:
#         file.close()


# ''' Type your code here. '''

# def main():
#     count=0
#     tracker={}

#     sentence=input().lower()
#     new=sentence.split(" ")

#     for word in new:
#         print(word)
#         #tracker[word]=count
#         if word in tracker:
#             count+=1
#             tracker[word]=count
#         if word not in tracker:
#             count=1
#             tracker[word]=count
#     print(tracker)

# main()



# Type your code here




# Type your code here


# def main():
#     print("Enter input string:")
#     name=input()
#     #name=name.strip()
    
#     if name=="q":
#         return None
#     elif "," not in name:
#         print("Error: No comma in string.")
#         print()
#         main()
#     else:
#         first, second=name.split(",")
#         first=first.strip()
#         second=second.strip()
#         print(f"First word:{first}")
#         print(f"Second word:{second}")
#         print()
#         main()

    
# main()
        


# specchar= ",!."
# frequency={}


# with open ("book.txt", "r") as file:
#     for line in file:
#         text=line.lower()

#     for char in specchar:
#         text=text.replace(char, " ")

#     words=text.split()

#     for word in words:
#         if word in frequency:
#             frequency[word]+=1
#         else:
#             frequency[word]=1

        
# print(frequency)
# print(text)


# inventory = ['sword', 'potion', 'map', 'coin']
# character_stats = ('STR', 8, 'DEX', 12)

# print(f"1. Starting inventory: {inventory}")
# chest_loot = ['scroll', 'coin', 'amulet']
# inventory.append(chest_loot)
# print(inventory)


# Read input and split input into tokens
# tokens = input().split()

# experiment_data = []
# for token in tokens:
#     experiment_data.append(int(token))

# print(f"All data: {experiment_data}")

# """ Your code goes here """
# sum_selected=0

# for i, token in experiment_data:
#     if int(token)>45 and i%2==0:
#         print(f"Index {i}: {token}")
#         sum_selected+=i
    

# print(f"Sum of selected elements is: {sum_selected}")

# # Read input and split input into tokens
# tokens = input().split()

# input_list = []
# for token in tokens:
#     input_list.append(int(token))

# print(f"Raw samples: {input_list}")

# ok_samples = 0

# """ Your code goes here """
# for i, token in enumerate(input_list):
#     if token>=35:
#         ok_samples+=1
#         print(f"Sample {i} is ok")
#     else:
#         print(f"Sample {i} needs attention")
    

# print(f"Total ok samples: {ok_samples}")



# actors = ["Pitt", "Damon"]
# actors.insert(1, "Affleck")
# print(actors[0], actors[1], actors[2])

# plants = input().split()
# colors = input().split()
# separator_char = input()

# """ Your code goes here """
# print(f"{"Plants":^19}|{"Colors":^19}")
# print(f"{plants[0]:>19}|{colors[0]:<19}")
# print(f"{plants[1]:>19}|{colors[1]:<19}")
# print(f"{plants[2]:>19}|{colors[2]:<19}")


# def unique(tester):
#     for i in range(len(tester)):
#         for j in range(i+1,len(tester)):
#             if tester[i] == tester[j]:
#                 return False
#     return True


# def main():
#     res1=unique("abcdefg")
#     res2=unique("hello")
#     print(res1, res2)

# main()



# skip_num = int(input())
# full_string = "raspberry"

# sliced_string=full_string[(len(full_string)//2)::skip_num]
# print("Full string:", full_string)
# print("Sliced string:", sliced_string)

# tax, income, status, wage= input("Enter here: ").split()

# print(tax)
# print(income)
# print(status)
# print(wage)


# status=int(input("enter: "))
# taxable=26000

# def main(status, taxable):
#     if status==0 or 1:
#             if 0<=taxable<=10000:
#                 return .1*taxable
#             elif 10001<=taxable<=40000:
#                 return 1000+(.12*taxable)
#             elif 40001<=taxable<=85000:
#                 return 4600+(.22*taxable)
#             elif 85000<=taxable:
#                 return 14500+(.24*taxable)
#     if status==2:
#         if 0<=taxable<=20000:
#             return .1*taxable
#         elif 20001<=taxable<=80000:
#             return 2000+(.12*taxable)
#         elif 80000<=taxable:
#             return 9200+(.22*taxable)

# gotit=main(2, 26000)
# print(gotit)



# one,two,three="1", "2", "3"
# print(two)
# print(one)
# print(three)

# a = 12 # 1100
# b = 10 # 1010

# print(a & b) # 8: 1000
# print(a | b) #14: 1110
# print(a ^ b) # 6: 0110

# print(4 ^ 5) #0100 and 0101 = 001

# age=int(input("enter your age: "))
# print(age)
# #print(type(age))

# if age>=16:
#     print("you can drive")
# else:
#     print("you cant drive")


# for i in range(1,6):
#     print(i, end=" ")
# print()

# print(5%2)
# total=0
# n=1
# while total <20:
#     total+=n
#     n+=1
# print(n,total)

####################in class practice with ZyBooks 11.7
# count=0
# n=int(input())

# while n>1:
#     print(n, end="\t")

#     if n%2==0:
#         n//=2
#     else:
#         n=(n*3)+1
#     count+=1

#     if count%5==0:
#         print("\n", end="")

# print(n, end="\t")

###########################

###################### in class practice with zybooks 13.8

# def countevens(num1, num2,num3,num4,num5):
#     count=0
#     if num1%2==0:
#         count+=1
#     if num2%2==0:
#         count+=1
#     if num3%2==0:
#         count+=1
#     if num4%2==0:
#         count+=1
#     if num5%2==0:
#         count+=1
#     return count

# countevens(20,21,86,3,1)

#####################


