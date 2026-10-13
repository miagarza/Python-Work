

def mystery(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            total += i
        elif i % 3 == 0:
            total += 2*i
        else:
            total -= i
        print("step", i, ":", total)
    return total


x=mystery(4)

def create_list(lst):
    new_list = []
    for item in lst:
        if item % 3 == 0:
            new_list.append(item * 2)
        else:
            new_list.append(item + 1)
    return new_list

x = mystery(4)
y = create_list([x, 3, 5])
print("x:", x)
print("y:", y)


# matrix=[[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(i,j)
#         print((i+j)%2)


# def compare_players(players, favorites):
#     common = ()

#     for i in range(len(players)):
#         for j in range(len(favorites)):
#             if players[i] == favorites[j]:
#                 if players[i] not in common:
#                     common += (players[i],)
#     print("Common players:", common)
#     print("Number of common players:", len(common))

#     for player in common:
#         print(player, "is at tuple index", players.index(player))

#     return common


# players = ("Jokic", "SGA", "Giannis", "Tatum", "Lebron")
# favorites = ["Curry", "Jokic", "Tatum", "Jokic", "Durant"]

# print(players[0])
# print(players[2])
# print(players[-1])
# print("Jokic count:", players.count("Jokic"))
# print("Tatum index:", players.index("Tatum"))

# result = compare_players(players, favorites)
# players[1] = "Curry"
# print("Done")



# # import math

# # print(math.sqrt(5) + 1)
# # print(math.sqrt(5))


# # grades = [
# #  [85, 90, 88], # Student 1's grades in Math, Science, and English
# #  [78, 82, 80], # Student 2
# #  [90, 85, 92], # Student 3
# #  [70, 75, 68] # Student 4
# # ]

# # avgs=[]
# # highest=[]

# # for i in grades:
# #     total=sum(i[:])
# #     avgs.append(total/3)

# #     highestone=max(i[:])
# #     highest.append(highestone)

# # #new_grades=list(dict.fromkeys(grades))

# # # for i in grades:
# # #     for j in i:
# # #         new_grades.add(j)

# # highest=tuple(highest)
# # print(avgs)
# # print(highest)
# # #print(new_grades)



# # # var=-2

# # # if var%2==0:
# # #     print("even")
# # # elif var%3==0:
# # #     print("three")
# # # else:
# # #     print("none")

# # # print(-2%2)
# # # print(-2//2)
